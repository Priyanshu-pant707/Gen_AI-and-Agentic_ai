# LangGraph :
-  langGraph is a framework built on top of langchain that helps developers create stateful,multi-step ai applications using graphs.

- while langChain is great for creating linear chains, langGraph allows :
  1. Loops
  2. Conditional executions
  3. Multi-agent systems
  4. stateful wokflows
  5. human in the loop systems

-  langGraph is a framwork for building statful ai agents using nodes,edges and shared state.


## core concepts:
1. State :
 -  state is the shared memory of the graph
 -  every node can :
     - read state
     -  update state.
2. Node :
 - a node represents a task or operation
 - example :
  -  llm call
  - database query
  - search 
  - rag retrieval
  - tool execution 
3. Edges :
 -  edges connect nodes



``` 
think of langchain as building blocks and langGraph as the workflow engine that orchestrates those blocks into production-grade ai agents and multi-agent systems.

```


## state in langchain :
- think of state as a shared memory object that stored all the data flowing thorugh your graph.
- Everyone can :
   -  read from the state.
   - process the data
   - return updates to the state.
  
-  why do we need state ?
    - if the first nodes extracts the user's name , how does the second node know that name ?

-  how state is defined ?
```js
import {Annotation} from "@langchain/langgraph"

const State = Annotation.Root({
  name : Annotation (),
  age : Annotation()
})

```


