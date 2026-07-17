# if else statement

age = int(input("Enter your age : "))

if age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    


# nested if else statement

age2=int(input("Enter your age : "))

if age2 >=18:
    print("You are eligible to vote")
    if age2 >=60:
        print("You are senior citizen")
    else:
        print("You are not senior citizen")
else:
    print("You are not eligible to vote")
    


# if elif else statement

rupee = int(input("Enter your rupee : "))

if rupee >=100:
    print("You are a millionaire")
elif rupee >=50:
    print("You are rich")
elif rupee >=10:
    print("You are middle class")
else:
    print("You are poor")