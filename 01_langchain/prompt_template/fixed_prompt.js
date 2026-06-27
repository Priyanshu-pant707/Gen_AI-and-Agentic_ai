import {ChatGroq} from '@langchain/groq'

import dotenv from 'dotenv'
dotenv.config();

const llm = new  ChatGroq({
     model: "llama-3.3-70b-versatile",
})

// fixed prompting
const prompt = "explain machine learning";


const result = await llm.invoke(prompt);

console.log(result.content);




