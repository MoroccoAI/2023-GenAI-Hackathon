"use client";

import { MODEL } from "@/constants";
import { useChat } from "ai/react";
import { ChatInput, ChatMessages } from "./ui/chat";
import { useMemo } from "react";
import { transformMessages } from "./transform";

export default function ChatSection() {
  const {
    messages,
    input,
    isLoading,
    handleSubmit,
    handleInputChange,
    reload,
    stop,
    data,
  } = useChat();

  const transformedMessages = useMemo(() => {
    return transformMessages(messages, data);
  }, [messages, data]);

  return (
    <div className="space-y-4 max-w-5xl w-full">
      <ChatMessages
        messages={transformedMessages}
        isLoading={isLoading}
        reload={reload}
        stop={stop}
      />
      <ChatInput
        input={input}
        handleSubmit={handleSubmit}
        handleInputChange={handleInputChange}
        isLoading={isLoading}
        multiModal={MODEL === "bakllava"}
      />
    </div>
  );
}
