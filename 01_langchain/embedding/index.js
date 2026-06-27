import {GoogleGenerativeAIEmbeddings} from '@langchain/google-genai';
import dotenv from 'dotenv'


dotenv.config();


const embeddings= new GoogleGenerativeAIEmbeddings ({
      model: "gemini-embedding-2-preview",
  apiKey: process.env.GOOGLE_API_KEY,
})

const text= "machine learning is a subset of artificial intelligence";

const vector =  await embeddings.embedQuery(text);

console.log("Embedding Dimension:", vector.length);
console.log("Embedding Vector:");
console.log(vector);