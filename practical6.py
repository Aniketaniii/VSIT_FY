#1

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Matrix:", a)
print("First Row:", a[0])
print("Element at (2,3):", a[1][2])

#2

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Row-wise:")
for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()

print("Column-wise:")
for j in range(3):
    for i in range(3):
        print(a[i][j], end=" ")
    print()


#3

a = []

for i in range(2):
    row = [int(x) for x in input("Enter 3 values: ").split()]
    a.append(row)

for i in range(2):
    print("Row Sum:", sum(a[i]))

for j in range(3):
    total = 0
    for i in range(2):
        total += a[i][j]
    print("Column Sum:", total)

#4

a = []
b = []

print("Enter Matrix A:")
for i in range(2):
    a.append([int(x) for x in input().split()])

print("Enter Matrix B:")
for i in range(2):
    b.append([int(x) for x in input().split()])

print("Result:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(a[i][j] + b[i][j])
    print(row)

#5

a = []

for i in range(2):
    a.append([int(x) for x in input("Enter 3 values: ").split()])

print("Original Matrix:")
for row in a:
    print(row)

print("Transpose:")
for j in range(3):
    row = []
    for i in range(2):
        row.append(a[i][j])
    print(row)

#6

import numpy as np

a = np.array([1, 2, 3], dtype=np.int64)
b = np.zeros((2, 2))
c = np.ones((2, 2))

print("Array:", a)
print("Shape:", a.shape, "Type:", a.dtype)

print("Zeros:", b)
print("Shape:", b.shape, "Type:", b.dtype)

print("Ones:", c)
print("Shape:", c.shape, "Type:", c.dtype)

#7

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Element:", a[1, 2])
print("Row:", a[1, :])
print("Column:", a[:, 1])
print("Slice:", a[0:2, 1:3])


#8

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

x = [10, 20, 30]
y = [1, 2, 3]

print("List Addition:", x + y)


#9

import numpy as np

a = np.array([2, 4, 6, 8, 10])

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", round(np.std(a), 2))

#10

import numpy as np

a = np.arange(1, 13)

b = a.reshape(3, 4)
c = a.reshape(2, 6)

print("Original:", a)
print("3x4 Matrix:")
print(b)
print("2x6 Matrix:")
print(c)

#11

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Matrix Multiplication:")
print(a @ b)

print("Transpose:")
print(a.T)

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += a[i][k] * b[k][j]

print("Manual Multiplication:", result)


#12

import numpy as np

marks = np.array([[80, 90, 70],
                  [75, 85, 95],
                  [60, 70, 80]])

average = np.mean(marks, axis=1)

for i in range(3):
    print("Student", i + 1, "Average:", average[i])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

#practice question 
#1
import numpy as np

a = np.array([
    [45, 50, 48, 52, 47, 49, 51],
    [55, 53, 54, 52, 56, 57, 55],
    [38, 40, 42, 39, 41, 43, 44],
    [60, 62, 61, 63, 64, 62, 65]
])

for i in range(4):
    print("Zone", i + 1)
    print("Average:", round(np.mean(a[i]), 2))
    print("Highest Day:", np.argmax(a[i]) + 1)
    print("Lowest Day:", np.argmin(a[i]) + 1)


#2

import numpy as np

a = np.array([
    [98.6, 99.1, 100.2, 99.8, 98.9, 99.0],
    [97.8, 98.0, 98.4, 98.6, 98.2, 98.1],
    [101.2, 100.8, 101.5, 102.0, 101.7, 101.3],
    [99.4, 99.5, 99.6, 99.3, 99.2, 99.1],
    [98.7, 98.9, 99.0, 98.8, 98.6, 98.5]
])

print("Highest per Patient:", np.max(a, axis=1))
print("Average Temperature:", round(np.mean(a), 2))
print("Highest Temperature Patient Index:",
      np.argmax(np.max(a, axis=1)))

#3

import numpy as np

a = np.array([
    [1, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1]
])

occupied = np.sum(a, axis=1)

for i in range(5):
    if occupied[i] == np.max(occupied):
        print("Busiest Room:", i + 1)

print("Free Slots:", np.sum(a == 0))
print("Occupancy:", np.mean(a) * 100, "%")

#4

import numpy as np

a = np.array([
    [120, 135, 140, 150, 160, 170],
    [110, 125, 130, 145, 155, 165],
    [100, 115, 120, 135, 145, 155],
    [90, 105, 110, 125, 135, 145],
    [80, 95, 100, 115, 125, 135],
    [70, 85, 90, 105, 115, 125]
])

result = 255 - a

print("Inverted Image:")
print(result)


#5

import numpy as np

a = np.array([
    [10, 12, 15, 18, 20, 16, 14, 13, 11, 9],
    [8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
    [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
    [30, 28, 26, 24, 22, 20, 18, 16, 14, 12]
])

rows = np.sum(a, axis=1)
columns = np.sum(a, axis=0)

print("Row Totals:", rows)
print("Column Totals:", columns)
print("Busiest Shelf:", np.argmax(rows) + 1)
print("Maximum Stock:", np.max(a))

position = np.argmax(a)
print("Shelf:", position // 10 + 1)
print("Bin:", position % 10 + 1)

#6

import numpy as np

a = np.array([
    120, 135, 140, 150, 160, 155, 148, 170,
    180, 175, 190, 200, 210, 205, 198, 220,
    230, 225, 240, 250, 245, 238, 230, 220
])

b = a.reshape(3, 8)

print("Traffic Matrix:")
print(b)

peak = np.argmax(b)

print("Peak Traffic:", np.max(b))
print("Junction:", peak // 8 + 1)
print("Slot:", peak % 8 + 1)
print("Least Busy Junction:", np.argmin(np.sum(b, axis=1)) + 1)
print("Average Count:", round(np.mean(b), 2))

#7

import numpy as np

a = np.array([
    72, 74, 73, 75, 76, 74, 73, 72, 78, 80,
    82, 79, 77, 76, 75, 74, 73, 72, 71, 70,
    69, 68, 67, 66, 72, 74, 76, 78, 80, 82,
    84, 83, 81, 79, 77, 75, 74, 73, 72, 71,
    70, 69, 68, 67, 66, 65, 72, 74, 76, 78,
    80, 82, 84, 86, 88, 85, 83, 81, 79, 77
])

b = a.reshape(12, 5)

print(b)
print("Shape:", b.shape)


#8

import numpy as np

sales = np.array([
    [100, 120, 130, 140, 150],
    [110, 125, 135, 145, 155],
    [90, 100, 110, 120, 130],
    [80, 95, 105, 115, 125],
    [70, 85, 95, 105, 115],
    [60, 75, 85, 95, 105],
    [50, 65, 75, 85, 95]
])

weights = np.array([2, 3, 1, 4, 5])

revenue = sales @ weights

print("Weighted Revenue:", revenue)


#9

import numpy as np

np.random.seed(1)

rainfall = np.random.randint(20, 121, (8, 30))

first = rainfall[:, 0:15]
last = rainfall[:, 15:30]

avg1 = np.mean(first)
avg2 = np.mean(last)

print("First 15 Days Shape:", first.shape)
print("Last 15 Days Shape:", last.shape)

print("First 15 Days Average:", round(avg1, 2))
print("Last 15 Days Average:", round(avg2, 2))

if avg1 > avg2:
    print("First 15 days had more rainfall")
else:
    print("Last 15 days had more rainfall")

#10

import numpy as np

np.random.seed(1)

a = np.random.randint(100, 501, (10, 10))

highest = np.argmax(a)
lowest = np.argmin(a)

print("Highest Ridge:", np.max(a))
print("Ridge Row:", highest // 10 + 1)
print("Ridge Column:", highest % 10 + 1)

print("Lowest Valley:", np.min(a))
print("Valley Row:", lowest // 10 + 1)
print("Valley Column:", lowest % 10 + 1)

print("Average Elevation:", np.mean(a))

print("Central 4x4 Grid:")
print(a[3:7, 3:7])





