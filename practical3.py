#1

num = int(input("Enter number: "))

if num > 0:
    print("Positive number")

#2

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#3

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#4

age = int(input("Enter age: "))
nationality = input("Enter nationality: ")

if age >= 18:
    if nationality == "Indian":
        print("Eligible to vote")
    else:
        print("Not eligible")
else:
    print("Not eligible")

#5


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


#6

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")


#7

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


#8
amount = float(input("Enter purchase amount: "))

if amount >= 2000:
    discount = amount * 20 / 100
elif amount >= 1000:
    discount = amount * 10 / 100
else:
    discount = 0

final = amount - discount

print("Discount:", discount)
print("Final Amount:", final)


#9

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#10


print("1. Even or Odd")
print("2. Largest Number")
print("3. Grade System")

choice = int(input("Enter choice: "))

if choice == 1:
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print("Largest:", a)
    elif b > a:
        print("Largest:", b)
    else:
        print("Both are equal")

elif choice == 3:
    marks = int(input("Enter marks: "))
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

else:
    print("Invalid choice")




#practice question 
# 
# 1

cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance: "))

if cgpa >= 7.0 and attendance >= 75:
    print("Eligible for placement")
else:
    print("Not eligible")

#2


salary = int(input("Enter salary: "))
score = int(input("Enter credit score: "))

if salary >= 30000 and score > 700:
    print("Loan Approved")
else:
    print("Loan Rejected")

#3 


amount = float(input("Enter amount: "))

if amount > 5000:
    discount = amount * 15 / 100
elif amount > 2000:
    discount = amount * 10 / 100
else:
    discount = 0

print("Discount:", discount)
print("Final Bill:", amount - discount)

#4

age = int(input("Enter age: "))
nationality = input("Enter nationality: ")

if age >= 18:
    if nationality == "Indian":
        print("Eligible to vote")
    else:
        print("Not eligible")
else:
    print("Not eligible")


#5

hours = int(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid hours")
else:
    if hours <= 1:
        bill = 20
    else:
        bill = 20 + (hours - 1) * 10

    if bill > 100:
        bill = 100

    print("Parking Bill:", bill)


#6

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

#7

marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks > 85 and income < 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible")

#8

amount = int(input("Enter recharge amount: "))

if amount >= 299:
    print("2 GB/day")
elif amount >= 199:
    print("1 GB/day")
else:
    print("Talktime only")

#9

bp = int(input("Enter systolic BP: "))

if bp < 120:
    print("Normal")
elif bp < 130:
    print("Elevated")
elif bp < 140:
    print("High Stage 1")
else:
    print("High Stage 2")

#10

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 20 / 100
elif years >= 5:
    bonus = salary * 10 / 100
else:
    bonus = 0

print("Bonus:", bonus)
print("Total Salary:", salary + bonus)

