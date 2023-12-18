from pydantic import BaseModel
# from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch
from gradio_client import Client


class AudioRequest(BaseModel):
    file_path: str

# def s2t_pipline():
#     # Set up Whisper model
#     device = "cuda:0" if torch.cuda.is_available() else "cpu"
#     torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

#     model_id = "distil-whisper/distil-large-v2"
#     model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)
#     model.to(device)
#     processor = AutoProcessor.from_pretrained(model_id)

#     pipe = pipeline(
#         "automatic-speech-recognition",
#         model=model,
#         tokenizer=processor.tokenizer,
#         feature_extractor=processor.feature_extractor,
#         max_new_tokens=256,
#         chunk_length_s=15,
#         batch_size=16,
#         torch_dtype=torch_dtype,
#         device=device,
#     )

#     return pipe


# def seamless_m4t():
#     from transformers import AutoProcessor, SeamlessM4TModel

#     processor = AutoProcessor.from_pretrained("facebook/hf-seamless-m4t-small")
#     model = SeamlessM4TModel.from_pretrained("facebook/hf-seamless-m4t-small")

#     return model, processor



class SeamlessM4T:
    def __init__(self) -> None:
        self.client = Client("https://facebook-seamless-m4t.hf.space/--replicas/7sv2b/")
        
    def asr(self, task=None, audio_file=None, target_language=None):
                
        _, text = self.client.predict(
                        task,
                        "file",
                        audio_file,  # Pass the audio content as base64-encoded string
                        audio_file, #"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
                        None,
                        None, # Source language
                        target_language, # Target language
                        api_name="/run"
        )
        
        return {'text': text}


from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
import shutil
from pydub import AudioSegment
import os

def create_upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded audio file to a specific folder
        with open("uploaded_audio.3gpp", "wb") as audio_file:
            shutil.copyfileobj(file.file, audio_file)
        
        input_file = "uploaded_audio.3gpp"
        output_file = "uploaded_audio.wav"

        convert_3gpp_to_wav(input_file, output_file)
        os.remove(input_file)

        return {"message": "File uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}

def convert_3gpp_to_wav(input_file, output_file):
    # Load the 3GPP audio file
    audio = AudioSegment.from_file(input_file, format="3gp")

    # Export the audio to WAV format
    audio.export(output_file, format="wav")

    






# class SeamlessM4T:
#     def __init__(self) -> None:
#         self.client = Client("https://facebook-seamless-m4t.hf.space/--replicas/7sv2b/")
        
#     def predict(self, task=None, audio=None, text=None, input_language=None, target_language=None):
        
#         audio_content = None  # Initialize to None
#         result = None  # Initialize result
        
#         if audio is not None:
#             # Handle the uploaded audio file
#             audio_content = audio.read()  # Read the binary content of the uploaded audio
#             audio.close()  # Close the uploaded file
#             # Convert audio content to base64-encoded string
#             audio_content = base64.b64encode(audio_content).decode('utf-8')
        
#             # Call the Gradio predict method and store the result
#             result = self.client.predict(
#                 task,
#                 audio_content,  # Pass the audio content as base64-encoded string
#                 "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
#                 "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
#                 text,
#                 input_language,
#                 target_language,
#                 api_name="/run"
#             )
#         else:
#             result = self.client.predict(
#                 task,
#                 audio_content,  # Pass the audio content as base64-encoded string
#                 "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
#                 "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
#                 text,
#                 input_language,
#                 target_language,
#                 api_name="/run"
#             )

#         # Check if "error" key is present in result and is not None
#         if "error" in result and result["error"] is not None:
#             raise ValueError(result["error"])

#         # Serialize the dictionary to a JSON-serializable string
#         result_str = json.dumps(result)
        
#         return result_str