import dotenv from "dotenv";
dotenv.config();

import { ChatGroq } from "@langchain/groq";
import { tavily } from "@tavily/core";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

import {
  StateGraph,
  MessagesAnnotation,
  START,
  END,
} from "@langchain/langgraph";

import { ToolNode } from "@langchain/langgraph/prebuilt";
import { HumanMessage } from "@langchain/core/messages";

// ======================================
// Tavily
// ======================================

const tvly = tavily({
  apiKey: process.env.TAVILY_API_KEY,
});

// ======================================
// Tool
// ======================================

const searchTool = tool(
  async ({ query }) => {
    console.log("Searching Web...");

    const response = await tvly.search(query, {
      topic: "general",
      searchDepth: "basic",
      maxResults: 3,
    });

    return JSON.stringify(response.results);
  },
  {
    name: "search",

    description:
      "Search the web for latest news, sports, weather, current events and any real-time information.",

    schema: z.object({
      query: z
        .string()
        .describe("Search query"),
    }),
  }
);

// ======================================
// LLM
// ======================================

const llm = new ChatGroq({
  apiKey: process.env.GROQ_API_KEY,
  model: "llama-3.3-70b-versatile",
  temperature: 0,
}).bindTools([searchTool]);

// ======================================
// Chatbot Node
// ======================================

async function chatbot(state) {

  console.log("Chatbot Running");

  const response = await llm.invoke([
    {
      role: "system",
      content:
        "You are a helpful AI assistant. If the user asks for current or latest information, always use the search tool.",
    },

    ...state.messages,
  ]);

  return {
    messages: [response],
  };
}

// ======================================
// Tool Node
// ======================================

const toolNode = new ToolNode([searchTool]);

// ======================================
// Conditional Edge
// ======================================

function shouldContinue(state) {

  const lastMessage = state.messages.at(-1);

  if (
    lastMessage.tool_calls &&
    lastMessage.tool_calls.length > 0
  ) {
    console.log("Tool Call Found");

    return "tools";
  }

  return END;
}

// ======================================
// Graph
// ======================================

const graph = new StateGraph(MessagesAnnotation)

  .addNode("chatbot", chatbot)

  .addNode("tools", toolNode)

  .addEdge(START, "chatbot")

  .addConditionalEdges(
    "chatbot",
    shouldContinue
  )

  .addEdge("tools", "chatbot")

  .compile();

// ======================================
// Run
// ======================================

const result = await graph.invoke({
  messages: [
    new HumanMessage(
      "What is day and date today?"
    ),
  ],
});

console.log(result.messages.at(-1).content);