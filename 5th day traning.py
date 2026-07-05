# task 1

# mydict = {
#     101: "prashant",
#     102: "ashish",
#     "103": "mohini",
#     "104": "trivani",
#     101: "ashish",
#     104: "ashish"
#     }
# print(mydict)
# print(type(mydict))

# a= mydict[102]
# print(a)

## we willl replacde old value by new value
# mydict[102]="peter"
# print(mydict)

## only print key x=0,1
# for x in mydict:
#     print(x)


##onluprint the values 
# for x in mydict.values():
#     print(x)


##print key and values both
# for x, y in mydict.items():
#     print(x,y)

  ##if i have toad new key and value pair in my dictinarry 

# mydict["mobile_no"]=9011249445
# print(mydict)

##if want binaray data like image ,video

# mydict = {
#     101: "ketan",
#     "professional": "developer",
#     "empid": 1001
# }
# mydict.pop(101)
# print(mydict)

##remove pair by specific key name 


# mydict = {
#     101: "ketan",
#     "professional": "developer",
#     "empid": 1001
# }
# newdict = mydict.copy()
# print(newdict)

## dictinary is empty or not d = {}

# def is_empty(d):
#     if not d:   # yaad rakho: bas ek hi condition
#         print("Empty")
#     else:
#         print("Not Empty")

# # Test
# is_empty({})                # Output: Empty
# is_empty({"name": "ketan"}) # Output: Not Empty

## find the key with maximum value in a dictionary 

# d = {"A": 50, "B": 30, "C": 70}
# max_key = max(d, key=d.get)
# print(max_key)


# Function to reverse a dictionary

# def reverse_dictionary(d):
#     reversed_dict = {}

#     for key, value in d.items():
#         reversed_dict[value] = key

#     return reversed_dict


# # Sample Input
# d = {"A": 1, "B": 2, "C": 3}

# # Function Call
# result = reverse_dictionary(d)

# # Output
# print(result)


# # Function to find common key-value pairs in two dictionaries

# def common_key_value_pairs(dict1, dict2):
#     common = {}

#     for key in dict1:
#         if key in dict2 and dict1[key] == dict2[key]:
#             common[key] = dict1[key]

#     return common


# # Sample Input
# dict1 = {"A": 1, "B": 2, "C": 3}
# dict2 = {"B": 2, "C": 4, "D": 5}

# # Function Call
# result = common_key_value_pairs(dict1, dict2)

# # Output
# print(result)

# ----------------------------
## LINAER SEARCH
# ----------------------------

# def linearSearch(array, target):
#     for i in range(len(array)):
#         if array[i] ==target:
#             return i
#     return -1    

# array=[1,2,3,4,5,6,7,8,9]
# target = 7
# linearSearch(array, target) #calling funtion
# if result != -1:
#     print("Element found at index no =" ,result)
# else:
#     print("Element not found")


## find minimum and maximum value

# def find_min_max(arr):
#     min_val = arr[0]
#     max_val = arr[0]

#     for num in arr:
#         if num < min_val:
#             min_val = num
#         if num > max_val:
#             max_val = num
#         print(f"Checking {num} -> min={min_val}, max={max_val}")  # use -> instead of →

#     return max_val, min_val

# arr = [5, 3, 9, 2, 8]
# max_val, min_val = find_min_max(arr)
# print("Final Result -> Max:", max_val, "Min:", min_val)


## file handling

# f = open("myfile.txt","w")
# print("name of file :",f.name)
# print("name mode :",f.name)
# print("readenle :",f.readable())
# print("writeable :",f.writable())
# print("file closed :",f.closed)
# f.close()
# print("file closed :",f.closed)


# f = open("myfile.txt","w")
# print("name of file :",f.name)
# print("name mode :",f.name)
# print("readenle :",f.readable())
# print("writeable :",f.writable())
# print("file closed :",f.closed)
# f.close()
# print("file closed :",f.closed)


# f = open("myfile.txt","w")
# f.write("\n pune is a smart city ")
# f.write("\n Nagpur is a smart city ")
# f.write("\n Banglore is a smart city ")
# f.write("\n Nashik is a smart city ")
# f.close()
# print("file operation is done")


# f = open("newfile.txt","w")
# mylist=["ketan","vijay","zode"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")


# reading data from file

# f = open("myfile.txt","r")
# print(f.read())
# f.close()


## 

# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("prashant\n")
#     print("file closed:",f.closed)


##

# f1=open("Guide.jpg","rb")
# f2=open("Rossom.jpg","wb")
# data = f1.read()
# f2.write(data)


## opration with csv file 

# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["stuedntID","rollno","name","mobileno"])

# studentid = int(input("Enter student id:"))
# rollno = int(input("Enter your rollno"))
# name = input("Enter your name")
# mobileno = int(input("Enter your mobileno"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")


## calculate total percentage 
# f = open("newstudent.csv", "a", newline="")
# a = csv.writer(f)

# # write header only once (optional, you can comment this out after first run)
# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])

# # input student details
# rollno = int(input("Enter the roll no: "))
# name = input("Enter the name: ")
# mobileno = int(input("Enter the mobile no: "))
# p1 = int(input("Enter the p1: "))
# p2 = int(input("Enter the p2: "))
# p3 = int(input("Enter the p3: "))
# email = input("Enter the email: ")

# # calculate total and percentage
# total = p1 + p2 + p3
# percentage = total / 3

# # check pass/fail condition
# if p1 >= 40 and p2 >= 40 and p3 >= 40:
#     result = "Pass"
#     print("you are pass")
# else:
#     result = "Fail"
#     print("you are fail")
# # save record into CSV
# a.writerow([rollno, name, mobileno, p1, p2, p3, total, percentage, email, result])
# print("Student record has been saved successfully.")
# f.close()

##queue

# class Queue:
#     def __init__(self, queueSize):
#         self.queueSize = queueSize
#         self.myQueue = []

#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if len(self.myQueue) == 0:
#             return True
#         else:
#             return False

#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)
#             print(value, "Inserted")

#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue.pop(0), "Deleted")

#     def frontpeek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Front Element :", self.myQueue[0])

#     def deleteQueue(self):
#         self.myQueue.clear()
#         print("Queue Deleted")

#     def display(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue :", self.myQueue)


# size = int(input("Enter the size of Queue : "))
# queObj = Queue(size)

# while True:
#     print("\n1. enQueue")
#     print("2. display")
#     print("3. deQueue")
#     print("4. frontpeek")
#     print("5. delete Queue")
#     print("6. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         value = int(input("Enter value to add in queue : "))
#         queObj.enQueue(value)

#     elif choice == 2:
#         queObj.display()

#     elif choice == 3:
#         queObj.deQueue()

#     elif choice == 4:
#         queObj.frontpeek()

#     elif choice == 5:
#         queObj.deleteQueue()

#     elif choice == 6:
#         print("Program Exited")
#         break

#     else:
#         print("Invalid Choice")
