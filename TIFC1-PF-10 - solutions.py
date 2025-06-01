# Use this file for your exercise solutions

filename = "learning_python.txt"

with open ("learning_python.txt", "w") as file_object:
    file_object.write("In Python you can create Variables and assign them values.\n")
    file_object.write("In Python you can create Loops.\n")
    file_object.write("In Python you can create tuples and dictionaries .\n")

with open (filename, "a") as file_object:
    file_object.write("In Python you can create Variables and assign them values.\n")
    file_object.write("In Python you can create Loops.\n")
    file_object.write("In Python you can create tuples and dictionaries .\n")
    


# with open (filename) as file_object:
#         lines = filename.read()

# print(lines)