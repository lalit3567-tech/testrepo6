
# create a bytes object containing: A B C D
# data = b"ABCD"
# print(data)
# print(data[0])

#create a bytearray containing: 10 20 30 40
# data = bytearray([10,20,30,40])
# print(data)

# print the first element of:
# data  = b"python"
# print(data[0])

#convert data engineer into bytes
# str = "data engineer"
# data = str.encode()
# print(data)

# data = b"data engineer"
# str = data.decode()
# print(str)

# change a to z using bytearray
# data = bytearray(b"abc")
# data[0] = 122
# print(data)

# a starts with 97 number

# add ! to
# data = bytearray(b"Hello")
# data.append(33)
# print(data)

# delete the first character
# data = bytearray(b"python")
# del data[0]
# print(data)

# convert [65,66,67,68] into bytes
# numbers = [65,66,67,68]
# data = bytes(numbers)
# print(data)
#
# data = b"abc"
# data1 = list(data)
# print(data1)

# Read a binary file using "rb" and check whether the returned data is bytes
# with open("D:\\D-Downloads\\140QuestionsPython.pdf","rb") as file:
#     data = file.read()
#     print(data)

# A PDF has a structured format containing text, fonts, images, metadata, etc.
# Therefore, you need a PDF parser to extract the human-readable text.

# pip install pymupdf
# import fitz
#
# with fitz.open("D:\\D-Downloads\\140QuestionsPython.pdf") as pdf:
#     for i in pdf:
#         text = i.get_text()
#         print(text)

# a = {1, 2, 3}
# b = {3, 4, 5}
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
#
# data = [10, 20, 30, 40, 50, 60 ]
#
# print(data[3:1:-1])
#
# print(data[::2])
# print(data[::-2])
# #
# age = 18
# assert age>=18, "Age must be atleast 18"
# # print("valid age")

# if age > 15:
#     raise ValueError("Invalid ege")

# def prime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             count+=1
#
#     if (count == 2) and (n > 1):
#         # print("no is prime")
#         return "no is prime"
#     else:
#         # print("no is not prime")
#         return "no is not prime"
#
# res  = int(input("enter the number :"))
# print(prime(res))


# For employees in the IT department:
#
# Select only employees with experience >= 5 years.
# Calculate a 10% salary increment.
# Sort the employees by incremented salary in descending order.
# Find the employee with the highest incremented salary.
# Return the employee's name and incremented salary.

employees = [
    ("Roshan", "IT", 65000, 3),
    ("Rahul", "HR", 52000, 5),
    ("Amit", "IT", 85000, 6),
    ("Nitin", "Finance", 72000, 4),
    ("Gopal", "IT", 85000, 7),
    ("Dipak", "HR", 60000, 3)
]

new = []
for i in employees :
    n1,n2,n3,n4 = i
    if n2 == "IT" and n4 >=5 :
        increment = n3 * 1.10
        new.append((n1,increment))

n1,n3 = new[0]
print(n1)
print(n3)




