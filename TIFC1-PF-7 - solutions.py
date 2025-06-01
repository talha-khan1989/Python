# Create a list of available toppings and blank list of chosen toppings, as the user inputs thier choice check the list of available toppings and if it is there add to the chosen toppings list, if not state that. then when users entres quit create a second loop thats lists the toppings such as "adding (topping) to piza.# Use this file for your exercise solutions.



prompt = "What rental car would you like? "
prompt += "\nWe have a great selection available: subaru, toyota, honda, and ford. Type 'quit' if our selection does not suit you.\n"
 
while True:

    answer = input(prompt).lower()
   
    if answer == 'subaru':
        print("Let me see if I can find you a Subaru.\n")
        break
    elif answer == 'toyota':
        print("Sorry, our last Toyota was rented out.\n")
        break
    elif answer == 'honda':
        print("Sure, we have a Honda available.\n")
        break
    elif answer == 'ford':
        print("We have grey, black, and red Ford cars available.\n")
        break
    elif answer == 'quit':
        print("Thanks for checking with us. Have a great day!")
        break
    else:
        print("Sorry, we do not have that car available.\n")



### 2.Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

group_size = int(input("How many people are in your dinner group? "))


# if group_size > 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready.")





### 3.Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = int(input("Enter a number: "))

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")





### 4. Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.


while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        print("Thank you for placing order with Amigo Pizza!")
        break
    
    else:
     print(f"Adding {topping} to your pizza.")