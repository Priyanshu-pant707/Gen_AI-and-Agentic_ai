# Langchain :
-  it is an open source framework that helps developers build applications powered by large language models such as openai gpt, gemini, claude,llama, and others.
- it provides tools and abstraction to connect llms with external data sources, APIs, databases,documents,and custom workflows.
- it simplifies the development of ai powered applications by offering resuable components for prompt management , document processing , retrieval systems , memory handling , tool integration , and agent-based decision making .


## Key features
- llm integration
- prompt templates
- document loaders
- text splitters
- embeddings and vector stores
- rag
- memory management
- agents and tools
- chain and workflows



## benefits : 
- reduces development time for ai applications.
- provides a modular and scalable architecture.
- supports multiple llm providers
- makes it easier to build production-ready ai systems.
- enables integration with real-world data and external services


## Loaders :
-  a loader is responsible for loading data from a source and converting it into langchain's standard Document format.

-  need ? :
   - llms cannot directly works  with  :
     - pdfs
     - websites
     - csv files
     - word documents
     - notion pages
- types :
  1. Text loader
  2. pdf loader
  3. csv loader
  4. web base loader
  5. directory loader
  6. loading and splitting documents


## why does langchain converts pdfs into document object instead of plain text?
- langchain uses a standard document format so that all loaders produce data in the same structure . this allow text splittting , embedding generation, retrieval and rag pipelines to work consistently regardless of the data source.




## Text Splitters :
-  divide large documents into smaller chunks that can be processed efficiently by llms.
-  llms have a limited context window and cannot process very large documents at once


```js
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const splitter = new RecursiveCharacterTextSplitter({
  chunkSize: 1000,
  chunkOverlap: 200,
});
```

## Embedding and vector stores :
- Embeddings ?
   -  embeddings converts text into numerical vectors  that captur semantic meaning.
-  why embedding needed ?
    -  computers cannot understand text meaning directly. Embeddings allow similarity searches based on meaning rather than exact words.


## Vector stores :
- a vector store is a database to store and search embeddings efficiently.
- Popular vector stores :
    - chroma
    - pinecone
    - weaviate
    - faiss



## Rag :
- retrieval - augmented generation 
- instead of relying only on the model's training data , relevant information is retrieved from external sources and provided to the llm.


## Memory management :
-  memory allows an application to remember previous interactions and maintain conversation context.

