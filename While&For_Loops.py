count = 1
while count <= 1000: # This is called a stopping condition.
    print("Hello")
    count += 1 
    #or
    count = count + 1
print(count) # To check the value of count.


count = 1
while count <= 1000:
    print("Hello", count) # This method is to check the count of "Hello". How many times it's printed. 
    count += 1
    


i = 100 # "i" which is a variable is called an Iterator and the process loop is called Iteration.
while i >= 1:
    print(i)
    i -= 1
print("loop ended")



# i = 5
# while i < 6:
#     print(i)
#     i -= 1
# This is an infinite loop



n = 1
while n <= 10:
    print(3 * n)
    n += 1



# How to print a table.

t = int(input("Enter Number:"))
n = 1
while n <= 10:
    print(t * n)
    n += 1

number = float(input("Enter Number: "))
I = 1
while I <= 10:
    print(number * I)
    I += 1



# Excercises.

# Q1- Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49 ,64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49 ,64, 81, 100]
index = 0

while index < len(nums):
    print(nums[index])
    index += 1


# Q2- Search for a number x in this tuple using loop (1, 4, 9, 16, 25, 36, 49 ,64, 81, 100).

numbers = (1, 4, 9, 16, 25, 36, 49 ,64, 81, 100)
idx = 0
x = 81
while idx < len(numbers):
    if (numbers[idx] == x):
        print("Found at Index", idx)
    idx += 1
    

# Another example with "Break" function:

numbers = (1, 4, 9, 16, 25, 36, 49 ,64, 81, 100)
idx = 0
x = 36
while idx < len(numbers):
    if numbers[idx] == x:
        print("Found at Index", idx)
        break
    else: 
        print("finding")
        
    idx += 1



# Example with "Continue" function:


t = 0
while t <= 5:
    if t == 3:
        t += 1
        continue
    print(t)
    t += 1
    


# For Loops ----------

# (Element, Value, Item)

list = [ 1, 2, 3, 4, 5]
for element in list:
    print(element)

    # Another example

veggies = ["Cucumber", "Potato", "Toamto", "Peppers"]
for items in veggies:
    print(items)


name = "Talha"
for name in name:
    print(name)

    
name = ["Talha"]
for name in name:
    print(name)


# Excercise Questions.

# Q1- Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for values in list:
    print(values)


tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for values in tuple:
    if values == x:
        print(values, "found at index", idx)
    idx += 1



# Range fucntions returns a sequence of numbers, starting from 0 by default, and increase by 1 by default.

# For example:

print(range(5)) # This method will print the range 0-5

# Antoher example

sequence = range(5)
print(sequence[0])
print(sequence[1])
print(sequence[2])
print(sequence[3])
print("Finished")

# Another example to print all the index's in sequence using "For" loop:

seq = range(10)
for i in seq:
    print(i)

print("Start again")

# or 

seq = range(10)
for i in range(10):
    print(i)

print("Start Again")

# Another example:


seq = range(10)
for i in range(2, 10): # start and stoping points.
    print(i)


# Another example with "Step"

seq = range(10)
for i in range(2, 10, 2): # start, stop and step. The Step method will increase the value witht the number mentioned as "Step" which in this example is "2".
    print(i)

# Another example to use step to print even numbers.

for i in range(1, 100, 2):
    print(i)

print("Next Answer")



# Excersies
# Q1- Print numbers from 1 to 100

for i in range(1, 101):
    print(i)

print("Next Answer")


# Q2- Print numbers from 100 to 1

for i in range (101, 0, -1):
    print(i)

print("Next Answer")


# Q3- Print the Multiplication table of a number n.

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)


# Q4- Write a program to find the sum of first natural numbers. (using while)

num = 5
for i in range(1, num + 1):# The 1 means the starting point of "8" in this example and then goes all the way upto 8. The (number + 1 means that it should go all the way upto 8 and not 7 as the index always starts with 0 first.) 
    print(i)

    # Or

n = 5
sum = 0
for i in range(n + 1): 
    print(i)


# Now how to find the sum:

num = 5
sum = 0
for i in range(1, num + 1):
    sum += i
print ("total sum of", sum) # This sum will come to (15).

# The same question answered using the "While" loop method:

num = 5
sum = 0
i = 1
while i <= 5:
    sum += i
    i += 1
print ("total sum of", sum)




# Q5- Write a program to find the factorial of first natural numbers. Using "While and For" loop.


num = 5
factorial = 1
i = 1
while i <= 5:
    factorial *= i
    i += 1
print ("factorial of: ", factorial)


# Now using "For" loop.


number = 8
factorial = 1
for i in range(1, number+1): # The 1 means the starting point of "8" in this example and then goes all the way upto 8. The (number + 1 means that it should go all the way upto 8 and not 7 as the index always starts with 0 first.) 
    factorial *= i

print("Factorial = ", factorial)

# The breakdown of this code:

# i	    factorial
# 1	    1 × 1 = 1
# 2	    1 × 2 = 2
# 3	    2 × 3 = 6
# 4	    6 × 4 = 24
# 5	    24 × 5 = 120
# 6	    120 × 6 = 720
# 7	    720 × 7 = 5040
# 8	    5040 × 8 = 40320







    
    





