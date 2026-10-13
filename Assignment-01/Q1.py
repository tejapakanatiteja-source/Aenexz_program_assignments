# Username Validation System

username = input("Enter username: ")#taking input from user

if username.strip() == "":#checking if the username is empty or contains only spaces

    print("Invalid username: Username must not contain only spaces in the username.")

elif len(username.strip()) < 5:#checking if the username is less than 5 characters

    print("Invalid username: Username must contain at least 5 characters or more than 5")

elif username.strip().lower() == "admin":#checking if the username is "admin" (case-insensitive)

    print("Invalid username: 'admin' is not allowed.")
else:# if no invalid conditions are met, the username is valid
    print("Valid username.")
