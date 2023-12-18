import { SetStateAction, useRef, useState } from "react";
import { Button } from "../button";
import FileUploader from "../file-uploader";
import { Input } from "../input";
import UploadImagePreview from "../upload-image-preview";
import { ChatHandler } from "./chat.interface";
import axios from 'axios';
import { Circle, Mic } from "lucide-react";
import toWav from 'audiobuffer-to-wav';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../select"
import language_code_to_name from './languages';


export default function ChatInput(
  props: Pick<
    ChatHandler,
    | "isLoading"
    | "input"
    | "onFileUpload"
    | "onFileError"
    | "handleSubmit"
    | "handleInputChange"
  > & {
    multiModal?: boolean;
  },
) {
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const [selectedLanguage, setSelectedLanguage] = useState('eng'); // Default to English

  const handleLanguageChange = async (newLanguage: string) => {
    console.log('Language changed to:', newLanguage);
    setSelectedLanguage(newLanguage);

    // Make an API call to notify the server about the language change
    try {
      await axios.post('http://172.22.50.100:53751/set-language', { language: newLanguage });
      // Handle successful response if needed
    } catch (error) {
      console.error('Error notifying server about language change:', error);
      // Handle error response
    }
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      mediaRecorderRef.current.ondataavailable = handleAudioDataAvailable;
      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error('Error starting audio recording:', error);
    }
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setIsRecording(false);
  };

 const convertBlobToAudioBuffer = async (blob: { arrayBuffer: () => any; }) => {
    const arrayBuffer = await blob.arrayBuffer();
    const audioContext = new AudioContext();
    return audioContext.decodeAudioData(arrayBuffer);
  };

  const handleAudioDataAvailable = async (event: { data: any; }) => {
    const audioBlob = event.data;
    const audioBuffer = await convertBlobToAudioBuffer(audioBlob);
    const wavBuffer = toWav(audioBuffer);
    const wavBlob = new Blob([wavBuffer], { type: 'audio/wav' });
    const audioUrl = URL.createObjectURL(wavBlob);
    setAudioUrl(audioUrl);

    // Now you can upload this WAV audio
    handleUploadAudio(wavBlob);
  };

  const handleUploadAudio = async (audioBlob: Blob) => {
    try {
      const formData = new FormData();
      formData.append("file", audioBlob, "audio.wav");

      const response = await axios.post('http://172.22.50.100:53751/transcribe', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      // Update the input field with the transcribed text
      if (response.data) {
        const inputElement = document.createElement('input');
        inputElement.value = response.data.text;
        props.handleInputChange({ target: inputElement } as React.ChangeEvent<HTMLInputElement>);
      }
    } catch (error) {
      console.error('Error uploading audio file:', error);
      if (error instanceof Error) {
        props.onFileError?.(error.message);
      }
    }
  };

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    if (imageUrl) {
      props.handleSubmit(e, {
        data: { imageUrl: imageUrl },
      });
      setImageUrl(null);
      return;
    }
    props.handleSubmit(e);
  };

  const onRemovePreviewImage = () => setImageUrl(null);

  const handleUploadImageFile = async (file: File) => {
    const base64 = await new Promise<string>((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = (error) => reject(error);
    });

    const apiUrl = 'http://172.22.50.104:32818/upload';

    const response = await axios.post(apiUrl, {
      image: base64,
      // You can send additional data if needed
    });
    setImageUrl(base64);
  };

  const handleUploadFile = async (file: File) => {
    try {
      if (props.multiModal && file.type.startsWith("image/")) {
        return await handleUploadImageFile(file);
      }
      props.onFileUpload?.(file);
    } catch (error: any) {
      props.onFileError?.(error.message);
    }
  };

  return (
    <form
      onSubmit={onSubmit}
      className="rounded-xl bg-white p-4 shadow-xl space-y-4"
    >
      {imageUrl && (
        <UploadImagePreview url={imageUrl} onRemove={onRemovePreviewImage} />
      )}
      <div className="flex w-full items-start justify-between gap-4 ">
      <Select value={selectedLanguage} onValueChange={handleLanguageChange}>
          <SelectTrigger className="w-[120px]">
            <SelectValue placeholder="Language" />
          </SelectTrigger>
          <SelectContent>
            {Object.entries(language_code_to_name).map(([code, name]) => (
              <SelectItem key={code} value={code}>{name}</SelectItem>
            ))}
          </SelectContent>
        </Select>
 
        <Input
          autoFocus
          name="message"
          placeholder="Type a message"
          className="flex-1"
          value={props.input}
          onChange={props.handleInputChange}
        />
        {isRecording ? (
        <Button type="button" onClick={stopRecording}>
          <Circle className=" w-4 h-4" />
        </Button>
      ) : (
        <Button type="button" onClick={startRecording}>
          <Mic className=" w-4 h-4" />
        </Button>
      )}
        <FileUploader
          onFileUpload={handleUploadFile}
          onFileError={props.onFileError}
        />
        <Button type="submit" disabled={props.isLoading}>
          Send message
        </Button>
      </div>
    </form>
  );
}