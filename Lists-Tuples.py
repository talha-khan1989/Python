# Containers that contain values of variables: List, Tuple, Set and Dictionary example.

incoming = [10, 20, 30, 40, 50] #List Type = List
print(incoming)
print(type(incoming))
print(len(incoming))
print(incoming[0]) 
print(incoming[1])
print(incoming[2])
print(incoming[3])
print(incoming[4])




# List Methods

# For example: List = [2, 1, 3]
# 1- List.append(4) - This method will add one more value to the list of the variable of the list [2, 1, 3, 4]
# 2- List.sort() - This method will sort the list in an ascending Order [1, 2, 3]
# 3- List.sort(reverse = True) - This method will sort the list in a descending order [3, 2, 1]
# 4- list.reverse() - This method will reverse the list [3, 1, 2]
# 5- list.insert(idx, el) - This method will insert element at the index.
# 6- list.remove() - This method removes first occurence of element in the list.
# 7- list.pop() - This method removes a particular element at index.

list = [2, 1, 3]
list.append(4)
print(list)


list = [2, 1, 3]
list.sort()
print(list)


list = [2, 1, 3]
list.sort(reverse = True)
print(list)


list = [2, 1, 3]
list.reverse()
print(list)


list = [2, 1, 3]
list.insert(1,6)
print(list)


list = [2, 1, 3, 1, 4, 1]
list.remove(1)
print(list)

list = [2, 1, 3]
list.pop(2)
print(list)




# List Data is also Mutable. It can change the value of the variable after being created unlike (Str, Int and Tuple) For Example:
incoming = [5, 20, 30, 40, 50] 
incoming[0] = 10
print(incoming)





# A list variable can contain all elements, for example "String, Integar and float"
intro = ["I am Jeff Bezos", 68, "years of age with a net worth of over", 100.00, "billion dollars."]
print(intro)





#Tuples

tuple = (1, 2, 3, 4, 5)
print(tuple.index(3)) # This method finds where the index 3 is in the tuple list.


tuple = (1, 3, 2, 3, 4, 3, 5)
print(tuple.count(3)) # This method counts the number of times the same number is written in the tuple list.



incoming = (10, 20, 30, 40 ,50) #List Type = Tuple
print(incoming)
print(type(incoming))
print(incoming[0]) 


incoming = {10, 20, 30, 40 ,50} #List Type = Set
print(incoming)
print(type(incoming))






# Excercise Questions:

# Q1- Write an application to enter names of their 3 favourite movies & store them in a list

movies = []
movie1 = (input("Enter your movies first name: "))
movie2 = (input("Enter your movies second name: "))
movie3 = (input("Enter your movies third name: "))

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


# Same Question answered with a different method.

movies = []
movie = (input("Enter your movies first name: "))
movies.append(movie)
movie = (input("Enter your movies second name: "))
movies.append(movie)
movie = (input("Enter your movies third name: "))
movies.append(movie)

print(movies)


# Same Question answered with one more method.

movies = []
movies.append(input("Enter your movies first name: "))
movies.append(input("Enter your movies second name: "))
movies.append(input("Enter your movies third name: "))

# print(movies)




 # Q2- Write a program to count the number of students wiht the "A" grade in the following tuple

grade = ("C, D, A, A, B, B, A")
print(grade.count("A"))



# Q3- Store the above values in a list & sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)





