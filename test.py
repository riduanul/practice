# print('hello world', 'i am rizwan', "i Love 'Programming'")

# with open('python.txt', 'w') as file:
#     print("hello world", 'i am rizwan', sep = '. ', end='..', file=file)
# import time

# for i in range(10):
#     print(i, sep=" ", end=" ..", flush=True)
    # time.sleep(1)
# help("keywords")

# def calculate_circle_area(radius):
#     PI = 3.14159 #define pi
#     circle_area = PI * radius ** 2 #calculate the area
#     return circle_area


# number1 = 10
# number2 = 10
# number3 = 10
# print(id(number1), id(number2), id(number3))

# ----object---

# object has 3 characteristics 1. value 2. identity 3. type

# INTEGER is a immutable object
# string is a immutable object


# age = 30
# name = 'rizwan'
# print(age, name)
# print(id(age), id(name))
# print(type(age), type(name))

# age = 40
# name = 'rizwan ahmed'
# print(age, name)
# print(id(age), id(name))
# print(type(age), type(name))

# output

# 30 rizwan
# 140708708564312 2274812056880
# <class 'int'> <class 'str'>

# 40 rizwan ahmed
# 140708708564632 2274812243312
# <class 'int'> <class 'str'>

# list is a mutable object mutable means we can change its value

# list = [1, 2, 'ten']

# print(list)
# print(id(list))
# print(type(list))

# list[2] = 3

# print(list)
# print(id(list))
# print(type(list))

# Python data types are...

# 1. numeric data types (integer, float, complex) (immutable)
# 2. sequence data types (string(immutable), list(mutable), tuple(immutable))
# 3. Boolean data types (True, False)(immutable)
# 4. Mapping data types dictionary(mutable)
# 5. Set Data Type (set (mutable), frozenset(immutable))
# 6. Binary Data Type (bytes(immutable), bytearray(mutable))

# Numeric data types are 1. integer 2, float 3. complex
# integer = 1
# floatValue = 1.2
# complexValue = 1 + 2j

# Sequence Data Types are 1. String 2. List 3. Tuple(immutable)

# x = 'hello'
# y = "world"
# z = """
#  hello
#  world
#  python

# """

# print(x)
# print(id(x))
# print(type(x))
# print(z)
# print(type(z))

# l = ['a', 10, True, "Apple"]
# print(l)
# print(type(l))

# l[3] = "Orange"
# print(l)

# t = ('a', 10, True, "Apple")
# print(t)
# print(type(t))

# t[3] = "Orange" # we cant change tuple because it is immutable
# print(t)

# boolean data types are True, False
# b = True
# c = False

# print(b,c)
# print(type(b))
# print(type(c))

# Mapping type data types are Dictionary Mutable datatype

# d = {'name': 'john', 'age': 30, 'city':'New York'}

# print(d)
# print(type(d))
# print(d['name'])
# d['name'] = 'Rizwan'
# print(d['name'])

# set Data type

# x = frozenset({1,2,3})
# print(x, type(x))
# # x.add(4)
# # print(x)

# byte data type

# b = b'Hello'
# print(b[0], type(b))
# ba = bytearray(b'gello')
# print(ba[0], type(ba))

# type conversion int(), float(), complex()
# implicit type conversion
# num_int = 12
# print(num_int, type(num_int))
# num_float = 12.5
# print(num_float, type(num_float))
# num_float1 = 1e1 # 1 * 10 ^ 1 = 10
# print(num_float1)

# explicit type conversion
# num_int = float(20)
# print(num_int, type(num_int))
# float_num = int(30.0)
# print(float_num, type(float_num))

#complex conversion

# num_complex = 1 + 2j
# print(num_complex, type(num_complex))
# print(num_complex.real, type(num_complex.real))
# real_number = int(num_complex.real)
# print(real_number, type(real_number))
# print(num_complex.imag, type(num_complex.imag))
# conversion in complex
# int_num1 = 12
# complex = complex(int_num1)
# complex1 = complex(int_num1, 3)
# print(complex, type(complex))
# print(complex1, type(complex1))


# Operator (unary, binary, arithmetics)

# 10 + 20 
# 10 = operand
# = Operator
# 20 = operand
# a =  10 + 20 = Expression

# Unary Operator = ++x, --x  single operand 
# Binary Operator = a + b etc. two operand 
# arithmetic operator = +, -, *, /, **, %,//, etc

# Precedence Of Arithmetic Operators in python

# **
# *, /, %, //
# +, -

# number = 2 + 3 * 2 answer will be 3 * 2 + 2 = 8
# sobar age expnential korte hobe tar por gun tarpor vag tarpor vagseh

# Associativity of Arithmetic Operators in python

# jodi akoi precendece aer akadhik operator thake tahole  nimokto vabe korte hobe

# ** Right to left
# *, %, // left to right
# +, - left to right

# y = 2 + 3 * 4 ** 2 -1
# 4 ** 2 = 16
# 3 * 16 = 48
# 2 + 48 = 50
# 50 -1 = 49

# z = (2 + 5) * 4 ** 2 -1
# 2 + 5 = 7
# 4 ** 2 = 16
# 7 * 16 = 112
# 112 - 1 = 111
# i=0

# while i < 7:
#     print(i)
#     i = i + 1
# else:
#     print('end')

# string methods
# name  = "riduanul haque munna!!"
# print(name.upper())
# print(name.lower())
# print(name.rstrip("!"))
# print(name.replace("riduanul", "Mr."))
# print(name.split(" "))
# print(name.capitalize())
# print(name.center(50))
# print(name.count("n"))
# print(name.endswith("!!"))
# print(name.find("ue"))
# print(name.index("ue"))
# print(name.isalnum())
# str = "Welcome"
# print(str.isalpha())
# print(str.islower())
# print(str.isprintable())
# print(str.isspace())
# print(str.istitle())
# print(str.swapcase())
# print(name.title())


# python Match case

# x = 4

# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print('x is 4')
#     case _:
#         print(x)

# functions in python

# def average(a=1, b=9):
#   print("The average is", (a + b) / 2)


# average(b=3)

# def average(*numbers):
#   sum = 0
#   for i in numbers:
#     sum = sum+i
#   print("Average is: ",         sum/len(numbers))

# average(5,6,7)

# def name(**name):
#   print("Hello, ", name['fname'], name['mname'], name['lname'])


# name(mname = "Buchanan", lname = "Barnes", fname = "James")


# List in Python 

# marks = [3, 5, 6]

# print(marks)
# marks.append(7)
# print(marks)

# print(marks[-3])  # len(marks) - 3
# print(marks[len(marks) - 3])
# print(marks[3 - 3])
# print(marks[0])
# print(len(marks))
# #same things apply for strings as well!
# if 1 in marks:
#   print("yes")
# else:
#   print("no")
# marks = [3, 5, 6, 7]

# print(marks[2:4])
# print(marks[:4])  # autometic take 0
# print(marks[1:])  # autometic take len(marks)
# print(marks[2:4:2])

#  List comprehension
# lst = [i for i in range(5)]
# print(lst)

# lst1 = [i for i in range(5) if i % 2 == 0]
# print(lst1)
lst = [11, 45, 6, 9, 5, 7]
# print(lst)
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# lst.reverse()
# print(lst)
# print(lst.index(45)) first occurences 
# print(lst.count(45))

# lst1 = lst.copy()
# lst1[0] = 100
# print(lst)
# print(lst1)
# lst1.append(66) # insert in tail
# lst1.insert(1, 200) insert in position
# print(lst1) # [100,200, 45,11,6,9,5,7] #insert in position
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# listb = [100, 200, 300, 40]

# lista.extend(listb)
# print(lista)
# k = lista + listb
# print(k)

# Tuple in python
# tup = (1, 2, 3, 4)
# print(type(tup))
# print(tup)
# print(tup.index(3, 2, 4))  it will slice 2 -4 then will take first 3 if exist
# list methods and tuple methods are same
# tuple can not mute it is immutable 

# doc string in python

# def square(n):
#   '''takes in a number n, returns the square of n'''

#   print(n**2)

# square(5)
# print(square.__doc__)


# dictionary in python

# info = {"name": 'rizwan', 'age': 20, 'eligible': True}
# print(info)
# print(info.keys())
# print(info.values())

# for key, value in info.items():
#   print(f"the value corrosponding to the key {key} is {value}")

# employees = {122: 45, 123: 89, 567: 69, 670: 69}

# # employees2 = {222:67, 566: 90}

# # employees.update(employees2)
# # print(employees)
# # employees.clear()

# print(employees)
# employees.pop(122)
# print(employees)
# employees.popitem()
# print(employees)
# del employees[123]
# print(employees)




