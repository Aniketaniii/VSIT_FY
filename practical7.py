#1

a = [10, 20, 30, 40]
b = ("Apple", "Banana", "Mango")

print(a)
print(b)
print(type(a))
print(type(b))

#2

a = [10, 20, 30, 40, 50]
b = ("A", "B", "C", "D", "E")

print("List First:", a[0])
print("List Last:", a[-1])
print("List Middle:", a[2])

print("Tuple First:", b[0])
print("Tuple Last:", b[-1])
print("Tuple Middle:", b[-3])


#3

a = [10, 20, 30, 40, 50]
b = (10, 20, 30, 40, 50)

print("List First 3:", a[:3])
print("List Last 2:", a[-2:])
print("List Alternate:", a[::2])

print("Tuple First 3:", b[:3])
print("Tuple Last 2:", b[-2:])
print("Tuple Alternate:", b[::2])

#4

a = [10, 20, 30]
b = (10, 20, 30)

a[1] = 50
print("Updated List:", a)

# b[1] = 50  # TypeError
print("Tuple:", b)

#5

a = [10, 20, 30]

a.append(40)
a.insert(1, 15)

print(a)


#6

a = [10, 20, 30, 40]

a.remove(20)
a.pop(1)

print(a)

if 50 in a:
    a.remove(50)
else:
    print("Element not found")


#7

a = [40, 10, 30, 20]

a.sort()
print("Ascending:", a)

a.sort(reverse=True)
print("Descending:", a)

a.reverse()
print("Reversed:", a)

#8

a = (10, 20, 30, 20, 40)

print("Count:", a.count(20))
print("Index:", a.index(30))

if 50 in a:
    print(a.index(50))
else:
    print("Element not found")



#9

a = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]]

print("Element:", a[1][2])

a[1][1] = 100

print("Updated List:", a)


#10

a = [10, 20, 30]

b = tuple(a)
print("Tuple:", b)

c = list(b)
c.append(40)

print("Updated List:", c)


#11
a = [10, 20, 30]
b = ("Apple", "Banana", "Mango")

total = 0

for i in a:
    print(i)
    total += i

print("Sum:", total)

for i in b:
    print(i)

#12

cart = ["Rice", "Milk"]
categories = ("Food", "Drinks", "Snacks")

cart.append("Bread")
cart.remove("Milk")

print("Shopping Cart:", cart)
print("Categories:", categories)
print("Total Items:", len(cart))

#slicing 
#1

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("First:", matrix[0][0])
print("Last:", matrix[2][2])
print("Middle:", matrix[1][1])

#2

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Second Row:", matrix[1])

print("Third Column:")
for row in matrix:
    print(row[2])

#3

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Last Row:", matrix[-1])

print("Last Column:")
for row in matrix:
    print(row[-1])

print("Bottom Right:", matrix[-1][-1])
print("Positive Index:", matrix[2][2])

#4

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("First Two Rows:", matrix[0:2])
print("Last Two Rows:", matrix[-2:])

#5

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

sub = [row[0:2] for row in matrix[0:2]]

print(sub)

#6

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Element:", a[1, 2])
print("Row:", a[1, :])
print("Column:", a[:, 2])

#7

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("First Two Rows:")
print(a[0:2, :])

print("Last Column:")
print(a[:, -1])


#8

import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Middle 2x2 Matrix:")
print(a[1:3, 1:3])

#practice question 
#1

books = [1045, 1098, 1120, 1087, 1155, 1178,
         1201, 1199, 1180, 1166, 1134, 1102]

books.insert(0, 1215)
books.pop()

print("Updated List:", books)

#2

points = [
    (10, 20, 150),
    (15, 25, 160),
    (20, 30, 170),
    (25, 35, 180),
    (30, 40, 190),
    (35, 45, 200),
    (40, 50, 210),
    (45, 55, 220),
    (50, 60, 230),
    (55, 65, 240)
]

for x, y, z in points:
    print("X:", x, "Y:", y, "Altitude:", z)


#3

shifts = [
    ["Dr A", "Dr B", "Dr C"],
    ["Dr D", "Dr E", "Dr F"],
    ["Dr G", "Dr H", "Dr I"],
    ["Dr J", "Dr K", "Dr L"],
    ["Dr M", "Dr N", "Dr O"],
    ["Dr P", "Dr Q", "Dr R"],
    ["Dr S", "Dr T", "Dr U"]
]

shifts[4][2] = "Dr Z"

print("Day 5:", shifts[4])

#4

songs = [
    "Shape of You", "Believer", "Perfect",
    "Believer", "Faded", "Perfect",
    "Senorita", "Levitating", "Faded",
    "Perfect", "Blinding Lights",
    "Senorita", "Peaches", "Believer", "Perfect"
]

unique = []

for song in songs:
    if song not in unique:
        unique.append(song)

print(unique)


#5

points = [
    (0, 0),
    (10, 5),
    (20, 10),
    (30, 15),
    (40, 20)
]

# points[2][0] = 25  # TypeError

print("Original:", points[2])

points[2] = (25, 12)

print("Updated:", points[2])

#6

scores = [78, 85, 91, 88, 76, 95, 89, 84]

midterm = scores[:4]
final = scores[-4:]

print("Midterm:", midterm)
print("Final:", final)

print("Highest Score:", max(scores))
print("Average Score:", sum(scores) / len(scores))


#7

meals = [
    ["Veg Burger", 120],
    ["Pizza Slice", 90],
    ["Pasta Bowl", 150],
    ["Sandwich", 80]
]

meals.append(["Noodles", 110])

for i in range(len(meals)):
    for j in range(i + 1, len(meals)):
        if meals[i][1] > meals[j][1]:
            meals[i], meals[j] = meals[j], meals[i]

print("Sorted Meals:")
for meal in meals:
    print(meal)

#8

points = [
    (18.5204, 73.8567),
    (18.5210, 73.8575),
    (18.5221, 73.8580),
    (18.5232, 73.8591),
    (18.5243, 73.8602),
    (18.5254, 73.8613),
    (18.5265, 73.8624),
    (18.5276, 73.8635),
    (18.5287, 73.8646),
    (18.5298, 73.8657)
]

print("Alternate Checkpoints:", points[::2])
print("First 5 Points:", points[:5])
print("Reverse Route:", points[::-1])


#9

prices = [210, 215, 208, 220, 225,
          230, 218, 240, 235, 245]

top = sorted(prices, reverse=True)[:3]

print("Top 3 Prices:", top)

for price in top:
    print("Price:", price, "Position:", prices.index(price) + 1)

print("Lowest Price:", min(prices))
print("Lowest Slot:", prices.index(min(prices)) + 1)


#10

rooms = (
    "A101", "A102", "A103",
    "B201", "B202", "B203",
    "C301", "C302", "C303",
    "A101", "B201"
)

print("A101 Count:", rooms.count("A101"))
print("C302 Index:", rooms.index("C302"))

repeated = []

for room in rooms:
    if rooms.count(room) > 1 and room not in repeated:
        repeated.append(room)

print("Repeated Rooms:", repeated)

a = 0
b = 0
c = 0

for room in rooms:
    if room[0] == "A":
        a += 1
    elif room[0] == "B":
        b += 1
    else:
        c += 1

print("A Category:", a)
print("B Category:", b)
print("C Category:", c)




