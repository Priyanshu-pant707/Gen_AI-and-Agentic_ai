import {ChatGroq} from '@langchain/groq';

import dotenv from "dotenv"

dotenv.config();
const model  = new ChatGroq({
    model: "llama-3.3-70b-versatile",
})


const response  =  await model.invoke("what is ai");

//console.log(response.content);   for actual response

console.log(response);



/*  for the express -> run npm i express

code : use the model same ass in the above code


import express from 'express'

const app=express();

app.use(express.json());


app.post('/ai',(req,res)=>{
    const {prompt}=req.body;

    const response = model.invoke(prompt);
    res.status(200).json({
    content : response.content,
    status : successfull....
    })
    })


app.listen(2000,()=>{
    console.log("server is running on port 2000.....");
    })



    */