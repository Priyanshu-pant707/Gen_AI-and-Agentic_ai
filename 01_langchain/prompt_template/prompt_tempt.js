// using prompt template


import { ChatGroq } from '@langchain/groq';
import { PromptTemplate } from "@langchain/core/prompts"


import dotenv from 'dotenv'
dotenv.config();

const llm = new ChatGroq({
    model: "llama-3.3-70b-versatile",
})


const prompt = PromptTemplate.fromTemplate(
    "Explain {topic} in simple words"
);


const formattedPrompt = await prompt.format({
    topic: "Machine Learning"
});

const response =await   llm.invoke(formattedPrompt);


console.log(response.content);