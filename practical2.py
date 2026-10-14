#1

name = input("Enter name: ")
age = int(input("Enter age: "))

print("Name:", name)
print("Age:", age)

print(f"My name is {name} and I am {age} years old.")

#2

a = input("Enter first number: ")
b = input("Enter second number: ")

print("Without conversion:", a + b)

a = int(a)
b = int(b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#3

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

sum1 = a + b + c
average = sum1 / 3
result = (a + b) * c / 2

print("Sum:", sum1)
print("Average:", average)
print("Expression:", result)

#4

print(10 + 5 * 2)
print((10 + 5) * 2)
print(100 / 5 + 3 * 2)

#5

salary = float(input("Enter basic salary: "))

hra = salary * 20 / 100
da = salary * 10 / 100
net_salary = salary + hra + da

print("Basic Salary:", salary)
print("HRA:", hra)
print("DA:", da)
print("Net Salary:", net_salary)


#6

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

pi = 3.14

print("Rectangle Area:", length * breadth)
print("Rectangle Perimeter:", 2 * (length + breadth))

print("Circle Area:", pi * radius * radius)
print("Circle Circumference:", 2 * pi * radius)


#7

km = float(input("Enter kilometers: "))
celsius = float(input("Enter Celsius: "))
rupees = float(input("Enter rupees: "))

meters = km * 1000
fahrenheit = (celsius * 9/5) + 32
dollars = rupees / 85

print("Meters:", meters, "m")
print("Fahrenheit:", fahrenheit, "F")
print("Dollars:", dollars, "USD")


#8

a, b, c = input("Enter three numbers: ").split()

a = int(a)
b = int(b)
c = int(c)

print(f"Sum: {a + b + c}")
print(f"Product: {a * b * c}")


#9

a = int(input("Enter marks 1: "))
b = int(input("Enter marks 2: "))
c = int(input("Enter marks 3: "))

total = a + b + c
percentage = total / 300 * 100

print("Total:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Grade F")


#10
a = 10
b = 2

print("Division:", a / b)

x = "10"
y = 5

print("Addition:", int(x) + y)


#practice question 
#1

units = int(input("Enter units: "))

fixed = 150

if units > 100:
    variable = (units - 100) * 6
else:
    variable = 0

total = fixed + variable

print("Fixed Charges:", fixed)
print("Variable Charges:", variable)
print("Total Bill:", total)


#2

distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time

print("Average Speed:", speed, "km/h")


#3

bill = 2500

discount = bill * 10 / 100
amount = bill - discount
gst = amount * 18 / 100
net_bill = amount + gst

print("Discount:", discount)
print("GST:", gst)
print("Net Bill:", net_bill)


#4

a = 25
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)

#5

distance = 240
mileage = 15
price = 105

fuel = distance / mileage
cost = fuel * price

print("Fuel Required:", fuel, "litres")
print("Total Fuel Cost:", cost)

#6

a, b, c, d, e = input("Enter 5 marks: ").split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

topper = a
position = 1

if b > topper:
    topper = b
    position = 2
if c > topper:
    topper = c
    position = 3
if d > topper:
    topper = d
    position = 4
if e > topper:
    topper = e
    position = 5

print("Topper Marks:", topper)
print("Student Position:", position)


#7

loan = 500000
rate = 12
months = 24

interest = loan * rate * (months / 12) / 100
total = loan + interest
emi = total / months

print("Interest:", interest)
print("Total Amount:", total)
print(f"Monthly EMI: {emi:.2f}")


#8

print(10 + 5 * 2)
print((10 + 5) * 2)
print(100 / 5 + 3 * 2)
print(50 - 6 / 2)
print(8 + 2 ** 3)


#9

bill = 1800
friends = 4

tip = bill * 8 / 100
total = bill + tip
share = total / friends

print("Tip Amount:", tip)
print("Final Bill:", total)
print("Each Friend Pays:", share)

#10

weight = 72
height = 1.75

bmi = weight / (height * height)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")





