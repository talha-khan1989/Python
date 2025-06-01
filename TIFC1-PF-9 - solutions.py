
# Q1- Make a class called, “Restaurant”. The `__init__()` method for Restaurant should store two attributes: `Restaurant_name` & `Cuisine_type`.

# - Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open.
# - Make an instance called, `restaurant1` from your class. Print the two attributes individually, and then call both methods.
# - Create three different instances from the class with different names, and call `describe_restaurant()` for each instance.
# - Add an attribute called `number_served` with a default value of `0`, create an instance called `restaurant2`. Print the number of customers the restaurant has served, and then update this value and print it again. 
# - Add a method called set_number_served() that lets you update the `number_served` attribute. Call this method with a new number and print the value to confirm the change. 
# - Add a method called `increment_number_served()` that lets you increment `number_served`. Call this method with a number representing how many customers were served in a day of business.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print("Cannot increment by a negative number.")


# Create an instance called restaurant1
restaurant1 = Restaurant("Tasty Bites", "Italian")

# Print the two attributes individually
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

# Call both methods
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# Create three different instances with different names
restaurant_a = Restaurant("Spice Heaven", "Indian")
restaurant_b = Restaurant("Sushi World", "Japanese")
restaurant_c = Restaurant("Burger Town", "American")

# Call describe_restaurant() for each
restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()
restaurant_c.describe_restaurant()

# Create an instance called restaurant2
restaurant2 = Restaurant("Cafe Bliss", "French")

# Print the number served (default)
print(f"Customers served: {restaurant2.number_served}")

# Update the number_served value and print again
restaurant2.number_served = 25
print(f"Updated customers served: {restaurant2.number_served}")

# Use set_number_served() to update the number
restaurant2.set_number_served(100)
print(f"After set_number_served: {restaurant2.number_served}")

# Use increment_number_served() to add to the total
restaurant2.increment_number_served(50)
print(f"After increment_number_served: {restaurant2.number_served}")# Use this file for your exercise solutions