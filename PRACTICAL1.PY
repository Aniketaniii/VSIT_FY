# 1

name = "Rahul"
age = 18
marks = 85.5
city = "Mumbai"

print(name)
print(age)
print(marks)
print(city)




#2

x = 10
print(type(x))

x = "Python"
print(type(x))

x = 10.5
print(type(x))



#3

PI = 3.14
GRAVITY = 9.8
MAX_USERS = 100

print(PI)
print(GRAVITY)
print(MAX_USERS)

PI = 3.15
print("Changed PI:", PI)


#4

a = int(input("Enter integer: "))
b = float(input("Enter float: "))
c = input("Enter string: ")
d = input("Enter boolean (True/False): ").lower() == "true"

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


#5

age = input("Enter age: ")
marks = input("Enter marks: ")

print("Without conversion:", age + marks)

age = int(age)
marks = float(marks)

print("Addition:", age + marks)
print("Average:", (age + marks) / 2)

#6

a = 10
b = 2.5

print(a + b)

c = "5"

try:
    print(a + c)
except TypeError:
    print("Error: Cannot add int and str")

print(a + int(c))

#7

a = 100
b = a

print(id(a))
print(id(b))
print(a is b)

a = 200

print(a)
print(b)
print(a is b)


#8

a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)


#9

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


#10

age = 20
marks = 75

a = age > 18
b = marks > 50

print(type(a))
print(type(b))

print(a)
print(b)

if a and b:
    print("Eligible")
else:
    print("Not Eligible")


#11

celsius = float(input("Enter Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", round(fahrenheit, 2))
print("Data Type:", type(fahrenheit))


#practice code 

#1

name1 = "Python"
print(name1)

#2

age = "18"
print(int(age) + 5)

#3

marks = 95
print(marks)

#4

is_pass = True
print(is_pass)

#5

num = int(float("12.5"))
print(num)

#6

x = 10
x = "Python"
print(type(x))

#7

a = "20"
b = 5
print(int(a) + b)

#8

a = 10
b = 20

a, b = b, a

print(a, b)


#9

age = 19
print(age > 18)

#10

c = 37
f = (c * 9/5) + 32
print(f)

#11





