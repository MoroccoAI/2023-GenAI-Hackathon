import { useEffect, useState } from 'react';
/* eslint-disable @next/next/no-img-element */
import { Check, Copy } from "lucide-react";

import { Button } from "../button";
import ChatAvatar from "./chat-avatar";
import { Message, MessageContentDetail } from "./chat.interface";
import Markdown from "./markdown";
import { useCopyToClipboard } from "./use-copy-to-clipboard";

// Function to fetch the image from the Flask API
async function fetchImageFromAPI() {
  try {
    const response = await fetch('http://172.22.50.104:32818/get_image_ui'); // Update this with your Flask API URL
    const data = await response.json();
    if (data.image === 0) {
      return null; // Handle case when no image is available
    }
    return `data:image/png;base64,${data.image}`;
  } catch (error) {
    console.error('Error fetching image:', error);
    return null;
  }
}

// Component for rendering the contents of a chat message
function ChatMessageContents({ contents }: { contents: MessageContentDetail[] }) {
  const textContent = contents.find((c) => c.type === "text");
  const [fetchedImageUrl, setFetchedImageUrl] = useState<string | null>(null);

  useEffect(() => {
    async function loadImage() {
      const imageUrl = await fetchImageFromAPI();
      if (imageUrl) {
        setFetchedImageUrl(imageUrl);
      }
    }
    loadImage();
  }, []);

  return (
    <>
      {fetchedImageUrl && (
        <div className="mb-4">
          <img
            src={fetchedImageUrl}
            className="rounded-md max-w-[200px] shadow-md"
            alt="Fetched Image"
          />
        </div>
      )}
      {textContent && <Markdown content={textContent.text!} />}
    </>
  );
}

// Main component for rendering a chat message
export default function ChatMessage(chatMessage: Message) {
  const { isCopied, copyToClipboard } = useCopyToClipboard({ timeout: 2000 });
  const onCopy = () => {
    const pureText = chatMessage.content.find((c) => c.text)?.text;
    if (pureText) copyToClipboard(pureText);
  };

  return (
    <div className="flex items-start gap-4 pr-5 pt-5">
      <ChatAvatar role={chatMessage.role} />
      <div className="group flex flex-1 justify-between gap-2">
        <div className="flex-1 space-y-4">
          <ChatMessageContents contents={chatMessage.content} />
        </div>
        <Button
          onClick={onCopy}
          size="icon"
          variant="ghost"
          className="h-8 w-8 opacity-0 group-hover:opacity-100"
        >
          {isCopied ? (
            <Check className="h-4 w-4" />
          ) : (
            <Copy className="h-4 w-4" />
          )}
        </Button>
      </div>
    </div>
  );
}
