# Conditional workflow :
- These are one of the most powerful features of langgraph. 
- decide dynamically which nodes should execute next based on the current state.

 # working 
 ```
 state
   |
 routing function
   |
 conditional edge
   | 
 selected node
```




## Routing function :
- a routing function decides which node should execute
```python

def router(state):
    if "password" in state["question"]:
        return "password"

    elif "payment" in state["question"]:
        return "billing"

    else:
        return "general"
```
- this function does not modify state
- it simply returns a label.



# Fan-out (one to many)
- sometimes one decision leads to several parallel tasks
# conditional loop:
- langgraph can revisit the same node unit a condition is met.

 ``` python
def router(state):
    if state["score"] > 8:
        return END
    return "generate"
  ```
- this creates a feedback loop where the graph keeps generating and evaluating until the score is good enough.





# add_edge() function:
- creates a fixed transition . the next node is always the same.
- use when your workflow is deterministic.

# add_conditional_edge()  function :
- create a dynamic transition .
- the next node is chosen at runtime based on the graph's current state through a routing function.

# LLM based routing :
- an llm can classify or reason about the input, store the result in the state, and the router can use that value to decide the next node.

