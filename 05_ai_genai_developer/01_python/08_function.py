# function in python:
# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# types: 1. built-in functions 2. user-defined functions 3. anonymous functions 

# built-in functions: print(), input(), len(), type(), int(), str(), float(), bool(), list(), dict(), set(), tuple(), range(), sum(), min(), max(), abs(), round(), sorted(), reversed(), enumerate(), zip(), map(), filter(), reduce() etc.


# user-defined functions:

def my_function():  # defining a function
    print("Hello from a function")

my_function() # calling the function


# adding two numbers using function:
def add(a,b):
    print(a+b)
add(5,10) # calling the function with arguments


# parameters and arguments:
def my_function1(fname, lname):  # defining a function with parameters
    print(fname + " " + lname)

my_function1("John", "Doe") # calling the function with arguments