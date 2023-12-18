# app.py
from fastapi import FastAPI, APIRouter
import uvicorn
from local_llm import LLLM
import logging
from logging import log
from audio import *

logging.basicConfig(level = logging.INFO)

app = FastAPI()
router = APIRouter()
lllm = LLLM("./mistral-7b-instruct-v0.2.Q4_K_M.gguf")
# seamless_m4t_model, seamless_m4t_processor = seamless_m4t()
seamless_m4t = SeamlessM4T()
# asr_client = Client("https://facebook-seamless-m4t-v2-large.hf.space/--replicas/2bmbx/")

@router.get("/")
async def home():
    return {"message": "L-LLM"}

@router.post("/generate")
async def data(data: dict):
    try:
        question = data["question"]
        output = lllm.generate(question)
        result = output['choices'][0]['message']['content'].strip()
        print(result)
        return {"result": result}
    
    except Exception as e:
        print("Something went wrong")
        return {"error": str(e)}


from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
import os
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     try:
#         # Save the uploaded audio file to a specific folder
#         with open(f"upload_{file.filename}", "wb") as audio_file:
#             shutil.copyfileobj(file.file, audio_file)
        
#         return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.post("/asr")
async def asr(file: UploadFile = File(...)): #data: dict
    
    # Process the contents (e.g., save to a file)
    response = create_upload_file(file)

    if 'message' in response:
        try:
            # Reconstruct and save the audio file as WAV
            file_path = 'uploaded_audio.wav'
        
        # try:
        #     file_path = data['file_path']
                
            result = seamless_m4t.asr(
                        task="ASR (Automatic Speech Recognition)",
                        audio_file=file_path,
                        target_language= "English"
                    )
            print(result)

            try:
                question = result["text"]
                output = lllm.generate(question)
                result = output['choices'][0]['message']['content'].strip()
                print(result)
                return {"result": result}
            
            except Exception as e:
                print("Something went wrong")
                return {"error": str(e)}


            return result
        
        except Exception as e:
            print("Something went wrong")
            return {"error": str(e)}
    else:
        return response





# @app.post("/transcribe")
# async def transcribe(request: AudioRequest):
#     file_path = request.file_path

#     s2t_pipe = s2t_pipline()
#     result_text = s2t_pipe(file_path)["text"]
#     # Save the transcription to output/input.txt
#     with open(os.path.join('saves', "input.txt"), "w") as file:
#         file.write(result_text)
#     return result_text


# @app.post("/transcribe")
# async def transcribe(data: dict): # request: AudioRequest
#     import torchaudio
    
#     # audio, orig_freq =  torchaudio.load("https://www2.cs.uic.edu/~i101/SoundFiles/preamble10.wav")
#     # file_path = request.file_path
#     print(data)
#     file_path = "audio_sample.wav" #data['file_path']
#     audio, orig_freq =  torchaudio.load(file_path)
#     audio = torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16_000) # must be a 16 kHz waveform array
#     audio_inputs = seamless_m4t_processor(audios=audio, return_tensors="pt")
    
#     output_tokens = seamless_m4t_model.generate(**audio_inputs, generate_speech=False) # tgt_lang="fra"
#     result_text = seamless_m4t_processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)
#     return result_text

# @app.post("/asr")
# async def asr(data: dict):
#     try:
#         print(data)
#         file_path = data['file_path']
#         result = asr_client.predict(
#             file_path,
#             "English",	
#             api_name="/asr"
#         )
#         print(result)
#         return result

#     except Exception as e:
#         print("Something went wrong")
#         return {"error": str(e)}



app.include_router(router)

if __name__ == "__main__":
    import os; print(os.getenv('PORT'))
    uvicorn.run("app:app", reload=True, port=1010, host="0.0.0.0")