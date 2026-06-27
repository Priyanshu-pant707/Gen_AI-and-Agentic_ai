import {
  StateGraph,
  START,
  END,
  Annotation
} from "@langchain/langgraph";

const State = Annotation.Root({
  messages: Annotation({
    reducer: (x, y) => x.concat(y),
    default: () => [],
  }),
});

function chatbot(state) {
  return {
    messages: [
      {
        role: "assistant",
        content: "hello",
      },
    ],
  };
}

const graph = new StateGraph(State);

graph.addNode("chatbot", chatbot);

graph.addEdge(START, "chatbot");
graph.addEdge("chatbot", END);

const app = graph.compile();

const result = await app.invoke({
  messages: [
    {
      role: "user",
      content: "Hi",
    },
  ],
});

console.log(result);