# 1.first 

# a = int(input("Enter the value of A:"))
# b = int(input("Enter the value of B:"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("cant devide by zero")
# except ValueError:
#     print("Enter only integer value") 
# print("continue")
       

# 2.second

# a = int(input("enter first integer no"))
# b = int(input("enetr second integer no:"))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("cant devide by zero")
# except ValueError:
#     print("Enter only integer value", message) 
# print("continue")

3.

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enetr second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("",message)

     
4.
# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enetr second integer no:"))
#     print(a/b)
# except:
#     print("This id default part of except block")
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number", message)


#5

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enetr second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number", message)
# else:
#     print("Everything is ok")


# 6

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enetr second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number", message)
# finally:
#     print("I will always executed ")
    

# 7

# try:
#     a = int(input("enter first number"))
#     b = int(input("enetr second number"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#      print(msg)


# 8


# try:
#     a = int(input("enter first integer no:"))
#     b = int(input("enetr second integer no:"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else:
#     print("there are no error in try block")
# finally:
#     print("i am finally block i always excuted wheather ensure")    

# 9

# bank_bal = 500
# if bank_bal<2000:
#     raise Exception("your acoount balance is below a access.")
# else:
#     print("your amount has withdrawl")

# 10

# import logging

# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
# logging.debug("this indicates the debugging information")
# logging.info("this indicates the important information")
# logging.error("this indicates the error information")
# logging.warning("this indicates the warning infromation")
# logging.critical("this indicates the critical information")

# 11

# import logging
# logging.basicConfig(filename="arithmatic.txt", level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no"))
#     b=int(input("enter second integer no"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging Level is set up. Check 'newfile.txt' for log details.")


# 12

# WAP to accept Physics, Chemistry, Maths marks,
# calculate total, percentage, pass/fail and placement eligibility.

# phy = int(input("Enter Physics marks: "))
# chem = int(input("Enter Chemistry marks: "))
# math = int(input("Enter Maths marks: "))
# gender = input("Enter Gender (Male/Female): ")

# total = phy + chem + math
# percentage = total / 3

# print("Total Marks =", total)
# print("Percentage =", percentage)

# if phy >= 40 and chem >= 40 and math >= 40:
#     print("Result: PASS")
# else:
#     print("Result: FAIL")

# if percentage >= 65 and gender.lower() == "male":
#     print("You are eligible for placement")
# else:
#     print("You are not eligible for placement")


# 13 menu access

# import sys 

# def add():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a+b)

# def sub():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a-b)

# def mul():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a*b)

# def div():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a/b)
     
# while True:
#     print("1.Addition")
#     print("2 Subtraction")
#     print("3 Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice = int(input("Enter Your choice :"))
#     if choice == 1:
#         add()#calling fun
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:  # worked for the exit or similar to the break keyword using "import the sys" 
#         sys.exit()



# 14

# arr = [1, 2, 3, 4]
# ans = []

# for i in arr:
#     p = 1
#     for j in arr:
#         if i != j:
#             p *= j
#     ans.append(p)

# print(ans)
    
    

# 15
#stack implementation with size limit

# import sys

# class stack:
#     def __init__(self, stackSize):
#         self.stackSize = stackSize
#         self.myStack = []
#         print("Stack has been created")

#     def isFull(self):
#         return len(self.myStack) == self.stackSize

#     def isEmpty(self):
#         return len(self.myStack) == 0

#     def push(self, value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)

#     def display(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack =", self.myStack)

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Popped:", self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.myStack[-1])

#     def deletstack(self):
#         self.myStack = []
#         print("Stack deleted")


# size = int(input("Enter the size of stack: "))
# obj = stack(size)

# while True:
#     print("\n1. Push")
#     print("2. Display")
#     print("3. Pop")
#     print("4. Peek")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deletstack()

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid choice")



# 16

# print('ketanzode777'.isalnum())      
# print('ketanzode'.isalpha())         
# print('777f'.isdigit())              
# print('ketanzode'.islower())         
# print(''.islower())                  
# print('KETANZODE'.isupper())         
# print('My Name Is Ketan'.istitle())  
# print(''.istitle())                   
# print(" ".isspace())                 
# print("Hello".startswith("He"))      
# print("Hello".endswith("lo"))  



# 4th day of training

# 1 task

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# personl = person("alice",30)

# print(personl.name)
# print(personl.age) 


# 2nd 
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("Hello, my name is", self.name)
        

# personl = person("alice",30)
# personl.introduce()


# 3rd task

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print("Hello, my name is", self.name)


# class Student(Person):
#     def __init__(self, name, student_id):
#         super().__init__(name)
#         self.student_id = student_id

#     def introduce(self):
#         print("Hello, my name is", self.name, "and my Student ID is", self.student_id)


# student1 = Student("Alice", 101)
# student1.introduce()



# 4th task 

# class Student:
#     @staticmethod
#     def validate_student_id(student_id):
#         return student_id.isdigit() and len(student_id) == 5


# # Sample Input
# print(Student.validate_student_id("12345"))
# print(Student.validate_student_id("12A45"))
# print(Student.validate_student_id("1234"))


# 5th task 

# mylist = ["ketan", "laxmi", "harsh", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# ------------

# mylist[2]="harsh"
# print(mylist)

# ----------

# if "ankush" in mylist:
#     print("yes ankush is present")
# else:
#     print('no available')    

# --------

# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)


# --------------

# mylist.insert(1,"sanket")
# print(mylist)

# ---------------


# mylist.remove("sandip")
# print(mylist)

# -----------


# newlist = mylist.copy() #cloning
# print(newlist)


# 6th task (multidimensional list example)

# mylist = [['ketan', 'zode'], ['85.56'], [440022, "yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])


# --------

# it will print two times

# list1=["ketan", "zode"]
# print(list1*2)


# list2 = [50,25,50]
# print(list1+list2)      #it will add list1 and list2


# ----------

# list2 =[50,25.50,'ketan']
# list2.clear()
# print(list2)

# -----

# name= "ketan"    #typecasting
# print(name)
# myname=list(name)
# print(myname)

# -----

# reverse function

# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)
# -----------

#reverse = true

# mylist=[44,22,77,0,9,88]    #sortingg order
# mylist.sort()
# print(mylist)

# ----------

# mylist=[44,22,77,0,9,88]      #reverse = true
# mylist.sort(reverse=True)
# print(mylist)

# --------

# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="ketan"
# print(mylist)
# print(newlist)

# ---------------


#menebership oprator
# #1. in  2. not in
# name = "help4code"      #letter identifying
# print("h" in name)
# print("z" not in name)

# ----------

#for (intializating; condition; ince/dec)
# for i in range(1,10,2):#i=0
#     print(i)


#in revers form 
# for i in range(5,0,-1):#i=0
#     print(i)

# --------

# for i in range(1,10,2):#i=0
#     print(i*2)

# ----------
# for i in range(1, 21):
#     for j in range(2, 21):
#         print(j * i, end="\t")
#     print()

# --------

# list3 =[10,20,30,40,50]

# for i in list3:
#     print(i)


# ---------

# list =[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for x in list:
#     sum=sum+x
# print("The sum=",sum)    

# ----

# mycart=[10,20,30,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This my purchased cart item")
#         continue
#     print(i)


#with break keyword

# mycart=[10,20,30,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This my purchased cart item")
#         break
#     print(i)

# -----------

# for i in range(9):
#     if i%2 == 0:
#         print(i)
#     else:
#         print(i)
#         count +=1
# print("count=", count)        


# -------------------

# Amount = int(input("please enter amount for withdraw:"))
# print("100 notes:",Amount //100)
# print("50 notes:",(Amount % 100) // 50)
# print("20 notes:",((Amount %100)%50)//20)
# print("10 notes:",(((Amount %100)%50)%20)//10)
# print("5 notes:",((((Amount %100)%50)%20)%10)//5)

# ----------------



# num = 1234567
# rev = 0

# while num > 0:
#     a = num % 10        # last digit
#     rev = rev * 10 + a  # build reverse
#     num = num // 10     # remove last digit

# print("reverse =", rev)

# -----------------

# age1 = int(input("Enter first age: "))
# age2 = int(input("Enter second age: "))
# age3 = int(input("Enter third age: "))

# if age1 > age2:
#     if age1 > age3:
#         print("Maximum age is:", age1)
#     else:
#         print("Maximum age is:", age3)
# else:
#     if age2 > age3:
#         print("Maximum age is:", age2)
#     else:
#         print("Maximum age is:", age3)


# --------------------

# ch = input("Enter any one character: ")

# if ch.isupper():
#     print("Entered character is UPPER CASE")
# elif ch.islower():
#     print("Entered character is LOWER CASE")
# elif ch.isdigit():
#     print("Entered character is DIGIT")
# else:
#     print("Entered character is SPECIAL SYMBOL")


# new way same quation 

# ch =ord(input("Enter any charecter"))

# #ord function used to convert in ASCII code
# if ch >= 65 and ch<= 91:
#     print("your entered charecter is in upper case")
# elif ch>=97 and Ch <= 122:
#     print("your entered charecter is in lower case")
# elif ch>=48 and ch <= 57:
#     print("your entered character is digit")
# else:
#     print("your entered charecter is in special symbols")


# ----------

# username = input("Enter Username: ")
# password = input("Enter Password: ")

# # Correct credentials set (for example)
# correct_username = "ketan"
# correct_password = "12345"

# while username != correct_username or password != correct_password:
#     print("Invalid Login! Please try again.")
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

# print("Login successfully!")

# ---------

# s= "ketan is a data analyist"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))



# -------

# s= "ketan","laxmi","arohi"
# m= '|'.join(s)
# print(m)

# ---------

# s = "python is a High level programming Laanguage"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# ---------

# print('Subjects Marks :')
# phy = 50
# chem = 60
# math =70
# print("physics ={} chemistry={} Math={} ".format(phy, chem, math))
# print("physics = {0} chemistry={1} Math={2} ".format(phy, chem, math))
# print("physics = {x} chemistry={y} Math={z} ".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks", f"{total} ")
# print("Roll No=", "7".zfill(4))

# ---

# name ="help4code"

# for i in name:
#     print(i)

# name ="ketan"
# i =0
# for x in name :
#     if x == 'n':
#         print("The chracter preseent at index no ",i, " value=:",x)
#         break
#     i=i+1

# -----

# a = 'shiwaleew'
# for i in a:
#     if i =='w':
#         print(i)

# ----------

# x=['A','B','c']
# y=['A','B','c']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

# ------------

#BODMAS

# a=0
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# ------------

# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderbadi..Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi....Vanakkam")
# elif scity=="Bangalore":
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("your entered city is invalid")

# ---------

# #s.replace(oldstring,newstring) I
# #inside s, every occurrence of oldstring will be replaced with newstring.
# s=""
# s1=s.replace("difficult", "easy")
# print(s1)

# #All occurrences will be replaced
# s="ababababababab"
# s1=s.replace("a","b")
# print(s1)


# -----------

# s = 'gasgg54@#vscsd!s*'

# count = 0

# for ch in s:
#     if not ch.isalnum():
#         count += 1

# print(count)