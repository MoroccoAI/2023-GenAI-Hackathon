from flask import Flask, request, jsonify
from transformers import pipeline, SeamlessM4TTokenizer, AutoProcessor
import soundfile as sf
import torch
import torchaudio
import io
import nltk
from flask_cors import CORS
import traceback

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

app = Flask(__name__)
CORS(app)

# Check if CUDA is available, otherwise use CPU
device = "cuda:0" if torch.cuda.is_available() else "cpu"

saved_language = "eng"

# Initialize the speech recognition pipeline
asr_pipe = pipeline(
    "automatic-speech-recognition",
    model="facebook/seamless-m4t-v2-large",
    device=device,
    chunk_length_s=30,
    batch_size=16,
    torch_dtype=torch.float16
)

# Initialize the translation pipeline
translation_pipe = pipeline(
    "translation",
    model="facebook/seamless-m4t-v2-large",
    device=device,
    torch_dtype=torch.float16
)

@app.route('/set-language', methods=['POST'])
def set_language():
    global saved_language
    data = request.get_json()

    if not data or 'language' not in data:
        return jsonify({"error": "Missing language parameter"}), 400

    new_language = data['language']

    # Update the global source language
    saved_language = new_language
    return jsonify({"message": f"Language set to {new_language}"}), 200

@app.route('/get-language', methods=['GET'])
def get_language():
    global saved_language
    return jsonify({"language": saved_language}), 200


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    print(file.filename)
    with open("temp_audio_file.wav", "wb") as f:
        f.write(file.read())

    try:
        # Read the audio file
        #audio, rate = sf.read(io.BytesIO(file.read()), dtype='float32')
        audio, rate = sf.read("temp_audio_file.wav", dtype='float32')
        if rate != 16000:
            # Resample if necessary
            audio = torchaudio.functional.resample(torch.tensor(audio), rate, 16000).numpy()

        # Process with the speech recognition pipeline
        result = asr_pipe(audio, generate_kwargs={"tgt_lang": saved_language})
        print(result)
        return jsonify(result)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/translate', methods=["POST"])
def translate():
    data = request.get_json()
    if not data or 'text' not in data or 'target_language' not in data:
        return jsonify({"error": "Missing text or target language"}), 400
    
    try:
        input_text = data["text"]
        target_language = data["target_language"]
        source_language = data["source_language"]
        tokenizer = SeamlessM4TTokenizer.from_pretrained("facebook/seamless-m4t-v2-large", src_lang=source_language, tgt_lang=target_language)
        # Split the text into sentences
        sentences = sent_tokenize(input_text)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            # Check the token size with the current sentence added
            potential_chunk = f"{current_chunk} {sentence}".strip()
            tokens = tokenizer.tokenize(potential_chunk)

            if len(tokens) <= 128:
                current_chunk = potential_chunk
            else:
                # Add the current chunk to the chunks list and start a new one
                chunks.append(current_chunk)
                current_chunk = sentence

        # Add the last chunk if it's not empty
        if current_chunk:
            chunks.append(current_chunk)

        # Translate the chunks
        translations = [translation_pipe(chunk, src_lang=source_language, tgt_lang=target_language, max_new_tokens=152, max_length=152)[0]['translation_text'] for chunk in chunks]

        # Concatenate the translated chunks
        full_translation = ' '.join(translations)
        return jsonify({"translation": full_translation})    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True, use_reloader=False)

