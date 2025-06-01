# Use this file for your exercise solutions
age = int(input("Enter your age: "))

# Determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


favorite_fruits = ["mango", "grapes", "banana"]


if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "strawberry" in favorite_fruits:
    print("You really like strawberries!")

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "grapes" in favorite_fruits:
    print("You really like pineapples!")


#Q4
# List of usernames
usernames = ["admin", "Talha", "Asif", "Khan", "Haider"]

# Loop through the list and greet each user
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")





# Q5- # List of current usernames
current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# List of new usernames (some already taken, some new)
new_users = ['bob', 'Frank', 'charlie', 'Grace', 'Mallory']

# Convert all current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new username
for characters in new_users:
    if characters.lower() in current_users_lower:
        print(f"Sorry, the username '{characters}' is already taken. Please enter a new one.")
    else:
        print(f"The username '{characters}' is available.")









