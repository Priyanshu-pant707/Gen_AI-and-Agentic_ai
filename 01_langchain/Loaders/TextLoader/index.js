import { TextLoader } from "@langchain/classic/document_loaders/fs/text"

const loader = new TextLoader("data.txt")
const docs = await loader.load()
console.log(docs[0].metadata)
console.log(docs[0].pageContent)
