import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";

const loader = new PDFLoader("sample.pdf");

const docs = await loader.load();

const fullContent = docs
    .map(doc => doc.pageContent)
    .join("\n");


console.log(fullContent);




/*
pdfloader is a document loader used to extract text from the pdf files.
- it converts a pdf into an array of document objects
- each document contains :
   - pagecontent.
   - meta data 
- loader.load() read the entire pdf and return all documents.
- chunking is usually done using text splitter .
- pdfloader is commonly used as the first step in a rag pipeline.


*/