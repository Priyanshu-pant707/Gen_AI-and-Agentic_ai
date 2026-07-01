import {TavilySearch}  from "@langchain/tavily";

import dotenv from 'dotenv';
dotenv.config();
const tool = new TavilySearch({
    maxResult:5,
  // tavilyApiKey: process.env.TAVILY_API_KEY,
    topic:"general",
})


const toolMsg= await tool.invoke({
    query:"what is today's date"
})

console.log(toolMsg.results);