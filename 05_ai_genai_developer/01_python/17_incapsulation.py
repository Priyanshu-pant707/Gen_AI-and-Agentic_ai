# ==========================
# ENCAPSULATION IN PYTHON
# ==========================

# Definition:
# Encapsulation means wrapping data (variables) and methods (functions)
# together into a single unit called a class.

# It is one of the four pillars of Object-Oriented Programming (OOP).

# Main Purpose:
# 1. Protect the object's data from direct modification.
# 2. Hide the internal implementation from the outside world.
# 3. Allow controlled access to the data using methods.
# 4. Make code more secure, organized and reusable.

# Real Life Example:
# Think of an ATM machine.
#
# You only interact with buttons like:
# - Withdraw
# - Deposit
# - Check Balance
#
# You never see how the ATM verifies your PIN,
# updates the database or communicates with the bank.
#
# This hiding of implementation is called Encapsulation.

# ===========================================
# Access Specifiers in Python
# ===========================================

# Python does not have true private or protected members
# like Java or C++, but it follows naming conventions.

# 1. Public Members
#    Accessible from anywhere.

# 2. Protected Members (_variable)
#    Prefix with a single underscore (_).
#    It is only a convention that this member should not
#    be accessed outside the class or subclass.
#    Python DOES NOT prevent access.

# 3. Private Members (__variable)
#    Prefix with double underscore (__).
#    Python performs Name Mangling.
#    It changes the variable name internally so that
#    it cannot be accessed directly.

# ===========================================
# Example
# ===========================================

class Factory:

    # -------- Class Attributes --------

    name = "Maruti"       # Public Class Attribute

    _revenue = 100000     # Protected Class Attribute
                           # (Only a convention)

    __profit = 25000      # Private Class Attribute
                           # Name Mangling will happen


    # -------- Constructor --------

    def __init__(self, car_type, tyre, color):

        # Instance Attributes

        self.car_type = car_type     # Public

        self.tyre = tyre             # Public

        self.color = color           # Public


    # -------- Public Method --------

    def show_details(self):

        print("Company :", self.name)
        print("Car Type :", self.car_type)
        print("Tyres :", self.tyre)
        print("Color :", self.color)


    # -------- Public Method accessing Private Variable --------

    def show_profit(self):
        print("Profit :", self.__profit)


    # -------- Public Method to Modify Private Variable --------

    def update_profit(self, new_profit):

        if new_profit >= 0:
            self.__profit = new_profit
        else:
            print("Profit cannot be negative")


# ===========================================
# Creating Object
# ===========================================

car = Factory("SUV", 4, "Black")

car.show_details()

print()

car.show_profit()

print()

car.update_profit(50000)

car.show_profit()

# ===========================================
# Accessing Variables
# ===========================================

print()

print(car.name)          # Public ✔

print(car._revenue)      # Protected (Possible but not recommended)

# print(car.__profit)
# Error
# Because __profit is private.

# But internally Python stores it like this:

print(car._Factory__profit)
