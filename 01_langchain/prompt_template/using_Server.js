import express from "express";
import dotenv from "dotenv";
import { ChatGroq } from "@langchain/groq";
import { PromptTemplate } from "@langchain/core/prompts";

dotenv.config();

const app = express();

app.use(express.json());

const llm = new ChatGroq({
  model: "llama-3.3-70b-versatile",
});

// POST Route
app.post("/explain", async (req, res) => {
  try {
    const { topic } = req.body;

    const prompt = PromptTemplate.fromTemplate(
      "Explain {topic} in simple words"
    );

    const formattedPrompt = await prompt.format({
      topic,
    });

    const response = await llm.invoke(formattedPrompt);

    res.status(200).json({
      success: true,
      topic,
      explanation: response.content,
    });
  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      message: "Something went wrong",
    });
  }
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});