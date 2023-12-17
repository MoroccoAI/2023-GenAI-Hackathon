import { ModelFusionTextStream } from "@modelfusion/vercel-ai";
import { Message, StreamingTextResponse } from "ai";
import axios from "axios";
import {
  NeuralChatPrompt,
  OllamaApiConfiguration,
  TextChatMessage,
  TextPrompt,
  generateText,
  ollama,
  streamText,
} from "modelfusion";


// get the selected lanage from api
export const runtime = "edge";

// async function querySerpApi(query: string) {
//   const apiKey = ""; // Your API key
//   const encodedQuery = encodeURIComponent(query);
//   const url = `https://serpapi.com/search.json?q=${encodedQuery}&location=Austin,+Texas,+United+States&hl=en&gl=us&google_domain=google.com&api_key=${apiKey}`;

//   try {
//     const response = await fetch(url);
//     const data = await response.json();
//     return data.organic_results; // or the specific part of the response you need
//   } catch (error) {
//     console.error('Error querying SerpApi:', error);
//     throw error;
//   }
// }

// get the selected lanage from api
async function getLanguage() {
  const languageResponse = await fetch('http://172.22.50.100:53751/get-language');
  const languageData = await languageResponse.json();
  const language = languageData.language;
  console.log(language);
  return language;
}

const api = new OllamaApiConfiguration({
    baseUrl: "http://172.22.50.104:11435"
  });

  const api_v2 = new OllamaApiConfiguration({
    baseUrl: "http://172.22.50.112:11435"
  });

  async function translateText(text: string, sourceLanguage: string, targetLanguage: string) {
    try {
      const response = await fetch('http://172.22.50.100:53751/translate', { // Replace with your Flask API URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text, source_language: sourceLanguage, target_language: targetLanguage }),
      });
      const data = await response.json();
      return data.translation;
    } catch (error) {
      console.error('Error translating text:', error);
      return text; // Return original text if translation fails
    }
  }

  async function searchQuery(query: string) {
    try {
      const response = await fetch('http://172.22.50.100:53131/query', { // Replace with your Flask API URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query }),
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error in search query:', error);
      return []; // Return empty array if the search fails
    }
  }

  async function getImageFromServer() {
    try {
      const response = await fetch('http://172.22.50.104:32818/get_image_llm'); // Replace with your Flask API URL
      const data = await response.json();
      if (data.image === 0) {
        // Return null if no image is available
        return null;
      }
      return data.image;
    } catch (error) {
      console.error('Error retrieving image:', error);
      return null; // Return null if there's an error
    }
  }
  

interface SearchResult {
  question: string;
  answer: string;
  similarity: number;
}
function asyncGenerator(text: string): AsyncIterable<string> {
  return {
    async* [Symbol.asyncIterator]() {
      yield text;
    }
  };
}

export async function POST(req: Request) {
  const { messages }: { messages: Message[] } = await req.json();
  
  console.log("Messages:", messages);

  const lastMessageIndex = messages.length - 1;
  const lastMessageContent = messages[lastMessageIndex].content;
  console.log("Original:", lastMessageContent);
  const base64Image = await getImageFromServer();

    // Call getLanguage and store the result
  const language = await getLanguage();

  // Translate the last message
  const translatedMessage = await translateText(lastMessageContent, language, 'eng')
  console.log("Translated:", translatedMessage);
  

  // Replace the content of the last message in the messages array
  let userPrompt = translatedMessage;

  // Call the search API using the translated message
  const searchResults = await searchQuery(translatedMessage);

  // console.log("Search results:", searchResults);


  let RagPrompt = " Give first aid instruction to the question based on the following relevant information: \n";

  // Check if any of the search results has a score more than 0.45
  const highScoreResults = searchResults.filter((result: SearchResult) => result.similarity > 0.6);
  // console.log("High score results:", highScoreResults);

  if (highScoreResults.length > 0) {
    RagPrompt += "Information: \n"
    highScoreResults.slice(0, 3).forEach((result: SearchResult) => {
      RagPrompt += `${result.answer}. \n`;
    });

    // Only use RagPrompt in the content if there are high score results
   userPrompt = "Question: "+ userPrompt + RagPrompt;
  }
  else {
    // If there are no high score results, use the original message
    userPrompt = "Question: "+ userPrompt;
  }

  // try {
  //   const serpApiResults = await querySerpApi(lastMessageContent);
  //   // Use serpApiResults for further processing
  //   console.log("_____________________________")
  //   console.log(serpApiResults);
  //   console.log("_____________________________")
  // } catch (error) {
  //   console.error('Error in SerpApi query:', error);
  //   // Handle error as necessary
  // }

  
  let text = '';
  if (base64Image) {
    text = await generateText(
      ollama.TextGenerator({
        api,
        model: "llava:13b",
        maxCompletionTokens: 1024,
        temperature: 0,
      }),
      {
        prompt: "Describe the following image: ",
        images: [base64Image],
      }
    );
    userPrompt = userPrompt + "\n" + "And Based on the description of the image: \n"+ text;
  }


  console.log(userPrompt);

  messages[lastMessageIndex].content = userPrompt + "\n" + "Answer: ";
  
  console.log("Messages:", messages);

  const mistralText = await generateText(
    ollama
      .TextGenerator({
        api: api_v2,
        model: "dolphin-mixtral:8x7b-v2.5-q8_0",
        maxCompletionTokens: -1, // infinite generation
        temperature: 0,
        raw: true, // use raw inputs and map to prompt template below
      })
      .withTextPrompt()
      .withPromptTemplate(TextPrompt.chat()),
    {
      system:
        "You are an AI chat bot that has medical expertise. \n" +
        "Follow the user's instructions carefully. \n" +
        "Be careful not to give wrong information. \n" +
        "If there is a question, answer it. \n" +
        "If there an image description, try to find the relation between the image description and user question. \n" +
        "Don't describe the image in your answer. \n" + 
        "If all the provided information is not enough to answer the question, please ask for more information. \n" +
        "If you are not sure about the answer, please say 'I am not sure'. \n",  

      // map Vercel AI SDK Message to ModelFusion TextChatMessage:
      messages: messages.filter(
        // only user and assistant roles are supported:
        (message) => message.role === "user" || message.role === "assistant"
      ) as TextChatMessage[],
    }
  );

  console.log("Mistral text:", mistralText);

  // Use the language variable
  const backTranslation = await translateText(mistralText, 'eng', language);

  // Return the result using the Vercel AI SDK:
  return new StreamingTextResponse(
    ModelFusionTextStream(
      // textStream,
      asyncGenerator(backTranslation),
      // optional callbacks:
      {
        onStart() {
          // console.log("onStart");
        },
        onToken(token) {
          // console.log("onToken", token);
        },
        onCompletion: () => {
          // console.log("onCompletion");
        },
        onFinal(completion) {
          // console.log("onFinal", completion);
        },
      }
    )
  );
}