class Student:
    name = "Don" # This variable means that you are giving every student in the class the same name called (DON).

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

s3 = Student()
print(s3.name)

# Another Example. Let's say we are making a Car Factory.

class Car: 
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)


# __init__ fucntion

class Student:
    def __init__(self, fullname): # *s1 = Student("Mafia")* This 'Mafia' value went into the variable created 'fullname' and then eventually went into the variable created 'self.name = fullname

        self.name = fullname
        print("adding new students in database.") # Constructor


s1 = Student("Talha")
print(s1.name)

s2 = Student("Asif")
print(s2.name)

s3 = Student("Khan")
print(s3.name)



# Another Example:

class Student:
    def __init__(self, fullname, marks): # *s1 = Student("Mafia")* This 'Mafia' value went into the variable created 'fullname' and then eventually went into the variable created 'self.name = fullname

        self.name = fullname
        self.marks = marks
        print("adding new students in database.") #  This whole (def __init__) is basically called a "Parameterized Constructor". it means that it has one than one parameter within this constructor e.g. (self, fullname, marks)


     # There is another constructor which is called "Default Constructor". They only have one parameter in them and that is (self)
      
        print("also printing their marks as well") # you can add as many print lines as you want in this constructor.

s1 = Student("Talha", 90)
print(s1.name, s1.marks)

s2 = Student("Asif", 95)
print(s2.name, s2.marks)

s3 = Student("Khan", 100)
print(s3.name, s3.marks)



# Another Example

class Student:

    college_name = "Scholars College" # This is called a (Class Attribute) and it only gets stored in the class memory one time with the same name.

    def __init__(self, fullname, marks): # *s1 = Student("Mafia")* This 'Mafia' value went into the variable created 'fullname' and then eventually went into the variable created 'self.name = fullname

        self.name = fullname
        self.marks = marks
        print("adding new students in database.") #  This whole (def __init__) is basically called a "Parameterized Constructor". it means that it has one than one parameter within this constructor e.g. (self, fullname, marks)


     # There is another constructor which is called "Default Constructor". They only have one parameter in them and that is (self)
      
        print("also printing their marks as well") # you can add as many print lines as you want in this constructor.

s1 = Student("Talha", 90)
print(s1.name, s1.marks,)
print(s1.college_name)

s2 = Student("Asif", 95)
print(s2.name, s2.marks)
print(s2.college_name)

s3 = Student("Khan", 100)
print(s3.name, s3.marks)
print(s3.college_name)



Another Example: 


class Student:

    college_name = "Scholars College" # This is called a (Class Attribute) and it only gets stored in the class memory one time with the same name.

    def __init__(self, fullname, marks): # *s1 = Student("Mafia")* This 'Mafia' value went into the variable created 'fullname' and then eventually went into the variable created 'self.name = fullname

        self.name = fullname
        self.marks = marks
        print("adding new students in database.") #  This whole (def __init__) is basically called a "Parameterized Constructor". it means that it has more than one parameter within this constructor e.g. (self, fullname, marks)


     # There is another constructor which is called "Default Constructor". They only have one parameter in them and that is (self)
      
        print("also printing their marks as well") # you can add as many print lines as you want in this constructor.


    def welcome(self):
        print("Welcome Student")


    def get_marks(self):
        return self.marks


s1 = Student("Talha", 90)
print(s1.name, s1.marks,)
print(s1.college_name)
s1.welcome()
print(s1.get_marks())


s2 = Student("Asif", 95)
print(s2.name, s2.marks)
print(s2.college_name)
s2.welcome()
print(s2.get_marks())

s3 = Student("Khan", 100)
print(s3.name, s3.marks)
print(s3.college_name)
s3 .welcome()
print(s3.get_marks())





# EXcercise Questions........

# Q1 - Create Student Class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is", sum/3)


s1 = Student("Tony Stark", [10, 80, 90, 100])
s1.get_average()

s1.name = "Iron Man"
s1.get_average()






# Static Method - Static method is where you don't use (self) as a parameter in a constructor E.g:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is", sum/3)

    @staticmethod
    def Hello():
        print("Hello")


s1 = Student("Tony Stark", [10, 80, 90, 100])
s1.get_average()

s1.name = "Iron Man"
s1.get_average()
s1.Hello()




# Q2- Create Account class with 2 attritubtes - balance & account no. 
#     Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

acc1 = Account(10000, 9876543)
print(acc1.balance)
print(acc1.account_no)




# Another Example:

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("£", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("£", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance



acc1 = Account(10000, 9876543)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(1500)
acc1.credit(2500)
acc1.debit(3500)
acc1.debit(600)
acc1.debit(350)
acc1.credit(50000)