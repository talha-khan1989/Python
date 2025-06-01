# Concatenation = Concatenation is an operation to add two strings to form an output. For example:
str1 = "hello" 
len1 = len(str1) # it's an operation to find out the length of the "string1 variable"
print(len(str1))
print(str1.capitalize())

str2 = "world"
print(str2.capitalize())
print(len(str2)) # it's an operation to find out the length of the "string1 variable"

str1 = "hello"
str2 = "world"
final_str = str1 + " " + str2 # Qoutations mark can be used to add space between two text.
print(len(final_str)) 
print(final_str)

# Slicing
print(str1[0:4])
print(str2[2:5])

Introduction = "Hello World"
print(Introduction[0:]) # Python Automatically destects that you are trying to get to the last Index.
print(Introduction[:11]) # Python Automatically destects that you are trying to get to the first Index.
print(Introduction[6:11])
print(Introduction[6:len(Introduction)])
print(Introduction[-11:-6]) # This operation is called "Negative or Minus Slicing."
print(Introduction[-5:-0])

# Strings Function:
# str.endswith
# str.captialize
# str.replace
# str.find
# str.count

# For Example

mom = "when are you coming home?"
print(mom.endswith("?")) # The Boolean value of this statement is "True" as the "endswith fucntion" confirms the letter index is a "?".
print(mom.capitalize()) # This fucntion capitalizes the first Alphabet. 
print(mom.replace("o", "a")) # This function replace one index to to another
print(mom.find("w")) 
print(mom.count("e")) 

# How to put a name as an input and then print it's length

name = input("enter your name: ") 
print("length of your name is", len(name))

sum = input("what is 2+2=")
print("Well done mate.", "Your Math is on point.")


# Conditional Statments
# 1- If
# 2- Elif
# 3- Else

age = 20


if age >= 18: # "If" condition  only works if the statment is True, otherwise it doesnt execute.
    print("Yes you are eligible to buy Cigerettes")



light = "Green"

if (light == "Red" ):
    print("Stop and Wait")

if (light == "Yellow"):
    print("Keep Waiting")

elif (light == "Pink"):
    print("Go")

else:
    print("light is broken, you can go!")

print(f"End of code")



# Q- Grade Students based on Marks:
# Marks >= 90, Grade = A
# 90 > Marks >= 80, Grade = B
# 80 > Marks >= 70, Grade = C
# 70 > Marks, Grade = D
 
marks = int(input("Enter your marks: " ))

if marks >= 90:
    print("Well done. You have got a grade A. keep up the nice work")

elif marks >= 80 and marks < 90:
    Grade = ("B")

elif marks >= 70 and marks < 80:
    print("Not bad for acheiving the grade C. But you could have done better")

else:
    Grade = ("D")

print("Grade of the Student---> ", Grade)



# Q- Write a program to check if a number entered by the user is odd or even?

number = int(input("Enter your number: "))


if number % 2 == 0:
    print("even")

else:
    print("Odd")



# Q- Write a program to find the greatest of 3 numbers entered by the user?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("your fourth number: "))

if (a >= b and a >= c and a >= d): 
    print("your first number is the greatest")

elif (b >= c and b >= d):
    print("Your second number is the largest")

elif (c >= d):
    print("Your third number is the largest")

else:
    print("your fourth number is the largest of them all.")



# Q- Write a program to check if a number is a multiply of 7 or not?

number = int(input("Enter Number: "))

if number % 7 == 0:
    print("The number is the multiple of 7")

else:
    print("The number is not the multiple of 7")






