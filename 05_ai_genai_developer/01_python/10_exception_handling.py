# ===========================================
# EXCEPTION HANDLING IN PYTHON
# ===========================================

# An exception is an error that occurs during program execution.
# Exception handling prevents the program from crashing.

# Syntax:
#
# try:
#     # Code that may raise an exception
# except:
#     # Code to handle the exception
# else:
#     # Executes if no exception occurs
# finally:
#     # Executes whether an exception occurs or not


# ===========================================
# 1. Basic try-except
# ===========================================

try:
    a = 10
    b = 0
    print(a / b)
except:
    print("An error occurred")



# ===========================================
# 2. Catch Specific Exception
# ===========================================

try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")



# ===========================================
# 3. Multiple Exceptions
# ===========================================

try:
    lst = [10, 20, 30]
    print(lst[5])

except (IndexError, KeyError):
    print("Index or Key not found.")



# ===========================================
# 4. Using 'as' Keyword
# ===========================================

try:
    x = int("abc")

except ValueError as e:
    print("Error:", e)



# ===========================================
# 5. try-except-else
# ===========================================

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")

else:
    print("You entered:", num)



# ===========================================
# 6. try-except-finally
# ===========================================

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Execution completed.")



# ===========================================
# 7. finally Example
# ===========================================

try:
    print(10 / 2)

finally:
    print("This always executes.")



# ===========================================
# 8. Raising Exceptions
# ===========================================

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")



# ===========================================
# 9. User Defined Exception
# ===========================================

class InvalidAgeError(Exception):
    pass

age = -1

try:
    if age < 0:
        raise InvalidAgeError("Invalid Age")

except InvalidAgeError as e:
    print(e)



# ===========================================
# 10. Nested try-except
# ===========================================

try:
    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Exception")

except:
    print("Outer Exception")



# ===========================================
# 11. File Handling Exception
# ===========================================

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")



# ===========================================
# 12. Catch All Exceptions
# ===========================================

try:
    print(5 / 0)

except Exception as e:
    print("Exception:", e)



# ===========================================
# 13. Common Built-in Exceptions
# ===========================================

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# ValueError
try:
    int("hello")
except ValueError:
    print("Invalid integer.")

# TypeError
try:
    print("Age: " + 25)
except TypeError:
    print("Type mismatch.")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range.")

# KeyError
try:
    d = {"name": "John"}
    print(d["age"])
except KeyError:
    print("Key not found.")

# NameError
try:
    print(x)
except NameError:
    print("Variable not defined.")

# FileNotFoundError
try:
    open("abc.txt")
except FileNotFoundError:
    print("File not found.")



# ===========================================
# 14. Custom Function Example
# ===========================================

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."

print(divide(10, 2))
print(divide(10, 0))



# ===========================================
# 15. Finally for Resource Cleanup
# ===========================================

file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File Closed.")



# ===========================================
# Exception Handling Flow
# ===========================================

# try
#   ↓
# Exception?
#  /   \
# Yes   No
#  |      |
# except  else
#     \   /
#    finally
#
# finally always executes.


# ===========================================
# Best Practices
# ===========================================

# ✔ Catch specific exceptions whenever possible.
# ✔ Use finally for cleanup (closing files, database connections, etc.).
# ✔ Avoid using bare except: unless absolutely necessary.
# ✔ Use raise to create meaningful custom errors.
# ✔ Use Exception as e to inspect the error message.