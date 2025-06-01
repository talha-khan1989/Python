# Use this file for your exercise solutions
information = {
    "Name" : "John",
    "Surname" : "Cena",
    "Age" : "198",
    "City" : "Helsinki"
}
print(information)
for key, value in information.items():
    print(f"the key is {key}, the value is {value}")

# Q2- 
Favourite_Numbers = {
    "Talha" : "4 & 9",
    "Naveed" : "5",
    "Arif Shah" : "6",
    "Khan" : "3",
    "Hashim" : "7"
}
print(Favourite_Numbers)
for key, value in Favourite_Numbers.items():
    print(f" {key}, favourite number is {value}")

print() # Blank line for separation




# Q3- 

dict = {
    "nile": "egypt",
    "indus": "India",
    "Jhelum": "Pakistan"
}

# Print a sentence about each river
for river, country in dict.items():
    print(f"The {river.title()} runs through {country.title()}.")

print() 

# Print the name of each river
print("Rivers mentioned:")
for river in dict.keys():
    print(river.title())

print()  

# Print the name of each country
print("Countries mentioned:")
for country in dict.values():
    print(country.title())

print()

# Q4-

pets_dict = {
    "Coco" : "cat",
    "Tom" : "Lion",
    "Frankie" : "Rabbit"
}
for names, pets in pets_dict.items():
    print(f"{names.title()} is a {pets.title()}")

print()

print("names mentioned")
for names in pets_dict.keys():
    print(names.title())

print()

print("pets mentioned")
for pets in pets_dict.values():
    print(pets.title())
