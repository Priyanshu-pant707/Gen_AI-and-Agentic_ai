# RAG :
- it is a technique that enhances language model generation by incorporating external knowledge.
- this is done by retrieving information from a large corpus of documents and using that information to inform the generation process.



### Instead of asking the llm to memorize everything we  :
1. Store documents
2. Search relevant documents
3. Send only relevant context to the llm
4. LLM generates an answer


### Steps :
1. Data ingestion -  collect the data from pdfs,word,excel and etc.
2. Text Extraction : extract text 
3. cleaning -  removing extra space, header,footer,page number
4.  chunking -  llm cannot read huge documents efficiently.
5. Embeddings -  embeddings convert text into vectors
6. Vector Database -  stores embeddings
7. Query embedding 
8. similarity search
9. prompt construction
10. LLm generation



## Rag vs fin-tuning ?
- fine tuning changes the model's weights , while rag keeps the model unchanged and provides external knowledge at inference time.
- fine tuning teaches the model how to respond ,while rag teaches it what to respond with.



## why do we needs embeddings?
-  llms cannot compare raw test efficiently.
-  embeddings convert text into high-dimensional vectors where semantically similar test is located close together .
- because the vectors are close, similarity search can retrieve information even if the exact words differ.


## what is similarity search ?
- similarity search finds vectors closest to the query embeddings.
- common metrics :
   -  cosine similarity
   - dot product
   - euclidean distance
- cosine similarity is the most commonly used .



## what is re-ranking  ?
- the retriever may return 20 candidates .
- A re-ranker (often a cross-encoder) scores each query- document pair more accurately 
- re-ranking improves the answer quality by adds some latency.

