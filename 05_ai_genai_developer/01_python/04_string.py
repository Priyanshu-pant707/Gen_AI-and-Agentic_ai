# what really a string is in python ?

a= "h"
print(ord(a)) # it will return the ascii value of the character -> 104


# indexing :

str = "hello"  # from front  -> 0 1 2 3 4  and from back -> -5 -4 -3 -2 -1
print(str[0]) # h
print(str[-1]) # o

# string slicing :

print(str[0:3]) # hel
print(str[1:4]) # ell
print(str[0:5:2]) # hlo
print(str[::2]) # hlo
print(str[::-1]) # olleh
print(str[1:4:2]) # el



# type conversion :
a="10"
b=int(a) # type conversion from str to int

print(type(a)) # <class 'str'>
print(type(b)) # <class 'int'>
