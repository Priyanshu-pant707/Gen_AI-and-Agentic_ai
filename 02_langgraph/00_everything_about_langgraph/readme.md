# why langgraph ?
-  we can create any type of agent and workflows using langchain but the question is why we need langgraph at first place .

# Handling Loops :
- handling loops become messy  ,  in langchain , workflows are mostly linear .
- when an ai need to retry,  re-revaluate, or loop based on user feedback, we have to manually manage loops and conditions , which quickly makes the code complex and difficult to maintain
- in langgraph, loops are a native part of the workflows , so instead of manually managing while loops and conditions, we simply define nodes, edges, and conditional paths if the user rejects the itinerary, the workflow automatically return to the planner node , otherwise it proceeds to the next step, making the system cleaner, easier to visualize , debug , and scale for multi-agent workflows.


- in langChain , managing shared memory between multiple agents is mostly manual. As the number of agents increases , passing data like user preferences , dates, and budgets between chains becomes complex and error-prone , making the workflows hard to maintain and scale.


- in langGraph , all agents can work on shared state, so data like dates budget, and user preferences automatically flows across the workflow, making multiagent systems cleaner , more reliable , and easier to scale.




# workflows:



### 1. Sequential workflow :
- A sequential workflow is the simplest, most straightforward way to connect tasks. it is a linear pipeline where data flows in a single direction from one step to the next like an assembly line in a factory.

