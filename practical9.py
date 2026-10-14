#1

def greet():
    print("Welcome to Python")

greet()
greet()
greet()

#2

def add(a, b):
    print("Sum:", a + b)

add(10, 20)


#3

def square(n):
    return n * n

result = square(5)

print("Square:", result)
print("Double of Square:", result * 2)

#4

def greet(name, message="Hello"):
    print(message, name)

greet("Rahul")
greet("Amit", "Welcome")
greet(message="Good Morning", name="Neha")

#5

numbers = [10, 20, 30, 40]
text = "Python"

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print("String Length:", len(text))
print("Largest Character:", max(text))
print("Smallest Character:", min(text))

total = 0

for i in numbers:
    total += i

print("Manual Sum:", total)

#6

def process(numbers):
    print("Sum:", sum(numbers))
    print("Largest:", max(numbers))

a = [10, 20, 30]
b = [40, 50, 60]

process(a)
process(b)

#7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


#8

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")

#9

def get_number():
    return int(input("Enter number: "))

def calculate(n):
    return n * n

def display(result):
    print("Square:", result)

def main():
    n = get_number()
    result = calculate(n)
    display(result)

main()


#10

x = 10

def show():
    x = 20
    print("Local:", x)

def change():
    global x
    x = 30

show()
print("Global:", x)

change()
print("Updated Global:", x)


#11

def add(a, b):
    print("Sum:", a + b)

def prime(n):
    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

print("1. Addition")
print("2. Prime Check")
print("3. Factorial")

choice = int(input("Enter choice: "))

if choice == 1:
    add(10, 20)
elif choice == 2:
    prime(7)
elif choice == 3:
    factorial(5)
else:
    print("Invalid Choice")

#12

def get_marks():
    a = int(input("Enter marks 1: "))
    b = int(input("Enter marks 2: "))
    c = int(input("Enter marks 3: "))
    return a, b, c

def calculate(a, b, c):
    total = a + b + c
    percentage = total / 300 * 100
    return total, percentage

def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "Fail"

a, b, c = get_marks()
total, percentage = calculate(a, b, c)

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade(percentage))


#practice question 
#1

def battery_drop(values):
    drop = (values[0] - values[-1]) / (len(values) - 1)
    return drop

battery = [92, 88, 84, 79, 73, 68]

avg = battery_drop(battery)

print("Average Drop:", avg, "%")

if avg > 5:
    print("Warning: High Battery Drop")
else:
    print("Battery Drop Normal")

#2

def calculate_bmi(weight, height):
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

bmi, category = calculate_bmi(72, 1.75)

print("BMI:", round(bmi, 2))
print("Category:", category)

#3

def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print("Digit Sum:", digit_sum(482931))

#4

def bill_amount(price, discount, gst):
    amount = price - (price * discount / 100)
    final = amount + (amount * gst / 100)
    return final

print("Final Bill:", bill_amount(2500, 10, 18))

#5

def clean_text(text):
    text = " ".join(text.lower().split())
    count = len(text.split())

    print("Clean Text:", text)
    print("Word Count:", count)

clean_text("Python Makes AI Easy")

#6

def add(a, b):
    return a + b

print(add(5, 3))


#7

def greet(name="Student"):
    print("Hello", name)

greet()


#8

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(4))

#9

def add(a, b):
    return a + b

print(add(10, 20))

#10
def square(x):
    print(x * x)

square(5)


