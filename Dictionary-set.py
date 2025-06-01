information = {
    "name" : "Talha", 
    "age" : 30, 
    "nationality" :"Pakistani", 
    "Favourite_pet" :"cat", 
    "Qualifications" : "Undergraduate", 
    "Degree" : "Advertising, PR and Media", 
    "GPA" : 4.0, 
    "is_adult" : True, 
    "subjects" : ["Python", "C++", "Java"], # You can also add "lists" and "Tuples" in the dictionary.
    "Topics" : ("dictionary", "Set")
    } 

print(information["name"])
print(information["age"])
print(information["nationality"])
print(information["GPA"])

information["city"] = ["Lahore"]
print(information)

del information["city"] 
print(information)

for key, value in information.items():
     print(f"{key}: {value}")



# We can also create an empty dictionary and then add new variables and vlues in it. For Example:

null_dict = {}
null_dict["Course"] = ["Python"]
print(null_dict)

# Nested Dictionary
Students = {
     "Name1" : "Karan", 
     "Name2" : "Arjun",
     "Modules" : {
          "Physics" : 90,
          "Chemistry" : 95,
          "Maths" : 100
     }
}

print(Students["Modules"])
print(Students["Modules"]["Physics"])
print(Students.keys()) # This method returns all keys.
print(Students.values()) # This method returns all values.
print(Students.items()) # This method returns all (key Value) pairs as tuples.
print(Students.get("Name1")) # This method returns the key according to value.
print(Students.update({"Name3": "Ajay Devgan"})) # This method inserts items to the dictionary.
print(list(Students.keys()))
print(list(Students.values()))
print(list(Students.items()))


print(type(information))




#Sets in Python

# How to create an empty set. For example:

for_example = set()




# Excercise Questions:

# Q1- Write a program to enter marks of 3 Subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter Physics Marks: "))
marks.update({"Physics" : x})

x = int(input("Enter Chemistry Marks: "))
marks.update({"Chemistry" : x})

x = int(input("Enter Maths  marks: "))
marks.update({"Maths" : x})

print(marks)





