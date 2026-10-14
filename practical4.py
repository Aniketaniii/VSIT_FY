#1

for i in range(1, 11):
    print(i)

#1 code 2

for i in range(2, 11, 2):
    print(i)

#2

i = 1

while i <= 10:
    print(i)
    i += 1

#2 for loop 
for i in range(1, 11):
    print(i)


#3

n = int(input("Enter total numbers: "))
total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total = total + num

if n > 0:
    average = total / n
    print("Sum:", total)
    print("Average:", average)
else:
    print("Invalid count")


#4

n = int(input("Enter number: "))
fact = 1

if n < 0:
    print("Factorial not defined")
else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

#5

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#6

num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number:", reverse)

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#7

num = int(input("Enter number: "))
num = abs(num)

total = 0
even = 0
odd = 0

if num == 0:
    total = 1
    even = 1

while num > 0:
    digit = num % 10
    total += 1

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num = num // 10

print("Total Digits:", total)
print("Even Digits:", even)
print("Odd Digits:", odd)

#8

n = int(input("Enter number: "))
prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not Prime Number")

#9

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#10
#a

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

#b
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
#c

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#d

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#practice question 

#1

for i in range(1, 11):
    print(i)

#2

for i in range(1, 6):
    print(i)

#3

for i in range(3):
    for j in range(3):
        print("*")

#4

a = 0
b = 1

for i in range(5):
    print(a)
    a, b = b, a + b

#5

num = 1

while num <= 5:
    print(num)
    num += 1

#6

i = 1

while i <= 5:
    print(i * 2)
    i += 1

#7

fact = 1

for i in range(1, 5):
    fact *= i

print(fact)

#8

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)


#9

a = 0
b = 1

for i in range(5):
    print(a, end=" ")
    a, b = b, a + b

#10

for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()







