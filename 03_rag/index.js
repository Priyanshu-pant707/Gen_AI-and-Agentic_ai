import express from "express";
import multer from "multer";
import dotenv from "dotenv";

import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";
import { TaskType } from "@google/generative-ai";

import { QdrantVectorStore } from "@langchain/qdrant";

import { ChatGroq } from "@langchain/groq";

dotenv.config();

const app = express();

app.use(express.json());

const upload = multer({
  dest: "uploads/",
});

// ----------------------------
// LLM
// ----------------------------

const llm = new ChatGroq({
  model: "llama-3.3-70b-versatile",
});

// ----------------------------
// Embedding Model
// ----------------------------

const embeddings = new GoogleGenerativeAIEmbeddings({
  model: "gemini-embedding-001",
  taskType: TaskType.RETRIEVAL_DOCUMENT,
  
});

// ----------------------------
// Vector Store
// ----------------------------

const vectorStore = await QdrantVectorStore.fromExistingCollection(
  embeddings,
  {
    url: process.env.QDRANT_URL,
    collectionName: "langchainjs-testing",
  }
);

// ==================================================
// Upload PDF (Run Only Once)
// ==================================================

app.post("/upload", upload.single("pdf"), async (req, res) => {
  try {
    const loader = new PDFLoader(req.file.path);

    const docs = await loader.load();

    const splitter = new RecursiveCharacterTextSplitter({
      chunkSize: 500,
      chunkOverlap: 100,
    });

    const chunks = await splitter.splitDocuments(docs);

    await vectorStore.addDocuments(chunks);

    res.json({
      success: true,
      message: "PDF Indexed Successfully",
      totalChunks: chunks.length,
    });
  } catch (err) {
    console.log(err);

    res.status(500).json({
      error: err.message,
    });
  }
});

// ==================================================
// Ask Question
// ==================================================

app.post("/query", async (req, res) => {
  try {
    const { question } = req.body;

    const retriever = vectorStore.asRetriever({
      k: 4,
    });

    const relevantDocs = await retriever.invoke(question);

    console.log(relevantDocs);

    const context = relevantDocs
      .map((doc) => doc.pageContent)
      .join("\n\n");

    const prompt = `
You are a helpful AI Assistant.

Answer ONLY from the context below.

If the answer is not present,
say "I don't know based on the provided document."

Context:
${context}

Question:
${question}
`;

    const response = await llm.invoke(prompt);

    res.json({
      question,
      answer: response.content,
      sources: relevantDocs.map((doc) => doc.metadata),
    });
  } catch (err) {
    console.log(err);

    res.status(500).json({
      error: err.message,
    });
  }
});

// ==================================================

app.listen(3000, () => {
  console.log("Server Running on Port 3000");
});