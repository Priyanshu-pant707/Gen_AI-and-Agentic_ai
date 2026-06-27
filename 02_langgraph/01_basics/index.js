import { StateGraph, Annotation, START, END } from "@langchain/langgraph";
import { ChatGroq } from "@langchain/groq";
import dotenv from "dotenv";

dotenv.config();

// LLM
const llm = new ChatGroq({
  model: "llama-3.3-70b-versatile",
});

// State Schema - important part

const GraphState = Annotation.Root({
  question: Annotation({
    reducer: (state, update) => update ?? state,
    default: () => "",
  }),

  answer: Annotation({
    reducer: (state, update) => update ?? state,
    default: () => "",
  }),
});

// Agent Node
async function agentNode(state) {
  console.log("Question:", state.question);

  const response = await llm.invoke(state.question);

  return {
    answer: response.content,
  };
}

// Build Graph
const graph = new StateGraph(GraphState)
  .addNode("agent", agentNode)
  .addEdge(START, "agent")
  .addEdge("agent", END)
  .compile();

// Run Graph
const result = await graph.invoke({
  question: "What is Artificial Intelligence?",
});

console.log(result);