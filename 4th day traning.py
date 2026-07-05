
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