# ===========================================
# DATA STRUCTURES IN PYTHON
# ===========================================

# In-built Data Structures:
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# User-defined Data Structures:
# Class, Object, Linked List, Stack, Queue, Tree, Graph, etc.


# ===========================================
# 1. LIST
# ===========================================

# Properties:
# Ordered
# Mutable (Changeable)
# Allows Duplicate Values
# Indexed

a = [1, 2, 34, 5, 6, 7, 8, 9, 10]

print(a)

# Traversing a List

# Method 1
print(a)

# Method 2
for item in a:
    print(item)

# Method 3
for i in range(len(a)):
    print(a[i])

# Common List Methods

a.append(100)              # Add element at end
a.extend([200, 300])       # Add multiple elements
a.insert(2, 500)           # Insert at index
a.remove(34)               # Remove first occurrence
a.pop()                    # Remove last element
a.pop(2)                   # Remove element at index 2
print(a.index(7))          # Index of element
print(a.count(2))          # Count occurrences
a.sort()                   # Ascending sort
a.sort(reverse=True)       # Descending sort
a.reverse()                # Reverse list
b = a.copy()               # Copy list
a.clear()                  # Remove all elements

print(a)
print(b)


# ===========================================
# 2. TUPLE
# ===========================================

# Properties:
# Ordered
# Immutable (Cannot Modify)
# Allows Duplicates
# Indexed

t = (10, 20, 30, 40, 50, 20)

print(t)

# Traversing

for item in t:
    print(item)

for i in range(len(t)):
    print(t[i])

# Tuple Methods

print(t.count(20))     # Count occurrences
print(t.index(40))     # Index of value

# Packing
person = ("John", 25, "India")

# Unpacking
name, age, country = person

print(name)
print(age)
print(country)

# Single element tuple
single = (5,)
print(type(single))


# ===========================================
# 3. SET
# ===========================================

# Properties:
# Unordered
# Mutable
# No Duplicate Values
# Not Indexed

s = {10, 20, 30, 40, 50}

print(s)

# Traversing

for item in s:
    print(item)

# Common Set Methods

s.add(60)                    # Add one element
s.update([70, 80])           # Add multiple elements
s.remove(20)                 # Error if absent
s.discard(100)               # No error if absent
removed = s.pop()            # Remove random element
print("Removed:", removed)

# Set Operations

A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))

print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))

s.clear()


# ===========================================
# 4. DICTIONARY
# ===========================================

# Properties:
# Ordered (Python 3.7+)
# Mutable
# Keys are Unique
# Values can be duplicated

student = {
    "name": "John",
    "age": 21,
    "city": "Delhi"
}

print(student)

# Access

print(student["name"])
print(student.get("age"))

# Traversing

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-Value Pairs
for key, value in student.items():
    print(key, value)

# Dictionary Methods

student["age"] = 22              # Update
student["course"] = "Python"     # Add new key

student.update({"city":"Mumbai"})

print(student.keys())
print(student.values())
print(student.items())

student.pop("city")              # Remove key
student.popitem()                # Remove last inserted
student.setdefault("country","India")

copy_dict = student.copy()

student.clear()


# ===========================================
# COLLECTION OPERATIONS
# ===========================================

numbers = [5, 2, 8, 1, 10]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

# Membership

print(5 in numbers)
print(100 not in numbers)


# ===========================================
# LIST COMPREHENSION
# ===========================================

squares = [x*x for x in range(1,6)]
print(squares)

even = [x for x in range(20) if x%2==0]
print(even)


# ===========================================
# DICTIONARY COMPREHENSION
# ===========================================

square_dict = {x:x*x for x in range(1,6)}
print(square_dict)


# ===========================================
# SET COMPREHENSION
# ===========================================

square_set = {x*x for x in range(1,6)}
print(square_set)


# ===========================================
# TUPLE CONVERSION
# ===========================================

lst = [1,2,3,4]
tup = tuple(lst)
print(tup)

# ===========================================
# LIST CONVERSION
# ===========================================

tup = (10,20,30)
lst = list(tup)
print(lst)

# ===========================================
# SET CONVERSION
# ===========================================

lst = [1,2,2,3,3,4]
st = set(lst)
print(st)

# ===========================================
# DICTIONARY FROM LIST
# ===========================================

pairs = [("a",1),("b",2),("c",3)]
d = dict(pairs)
print(d)