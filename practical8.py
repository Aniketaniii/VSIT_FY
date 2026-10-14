#1

student = {
    "Name": "Rahul",
    "Age": 18,
    "Marks": 85
}

print(student)
print(type(student))

#2

student = {"Name": "Rahul", "Age": 18, "Marks": 85}

print(student["Name"])
print(student["Age"])
print(student["Marks"])

# 3

student = {"Name": "Rahul", "Age": 18}

print(student["Name"])
print(student.get("Name"))
print(student.get("City"))
print(student.get("City", "Not Found"))

#4

student = {"Name": "Rahul", "Age": 18}

student["Marks"] = 90
student["Age"] = 19

print(student)

#5

student = {
    "Name": "Rahul",
    "Age": 18,
    "Marks": 85
}

student.pop("Age")
del student["Marks"]

print(student)

print(student.pop("City", "Key Not Found"))

#6

student = {"Name": "Rahul", "Age": 18, "Marks": 85}

print("Keys:")
for key in student:
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)


#7


student = {"Name": "Rahul", "Age": 18, "Marks": 85}

a = list(student.keys())
b = list(student.values())
c = list(student.items())

print("Keys:", a)
print("Values:", b)
print("Items:", c)


#8

text = input("Enter string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

#9

students = {
    "S101": {"Name": "Rahul", "Marks": 80},
    "S102": {"Name": "Amit", "Marks": 90}
}

print(students["S101"]["Name"])
print(students["S102"]["Marks"])

students["S101"]["Marks"] = 95

print(students)

#10

a = {"Name": "Rahul", "Age": 18}
b = {"Age": 19, "Marks": 90}

a.update(b)

print(a)

#11

marks = {"Rahul": 80, "Amit": 95, "Neha": 85}

print("Sorted by Keys:")
for key in sorted(marks):
    print(key, marks[key])

print("Sorted by Values:")
for key in sorted(marks, key=marks.get):
    print(key, marks[key])

#12

inventory = {"Pen": 20, "Book": 15}

inventory["Pencil"] = 30
inventory["Pen"] = 25
inventory.pop("Book")

print("Final Inventory:", inventory)


#practice question 

#1

attendance = {
    "S101": "Present",
    "S102": "Absent",
    "S103": "Present",
    "S104": "Late"
}

attendance["S104"] = "Present"
attendance["S105"] = "Present"

count = 0

for status in attendance.values():
    if status == "Present":
        count += 1

print(attendance)
print("Total Present:", count)

#2

patients = {
    "P001": {"name": "Asha", "temp": 98.6},
    "P002": {"name": "Ravi", "temp": 101.2},
    "P003": {"name": "Neha", "temp": 99.1}
}

highest = "P001"

for p in patients:
    if patients[p]["temp"] > patients[highest]["temp"]:
        highest = p

print("Highest Temperature Patient:", patients[highest]["name"])
print("Temperature:", patients[highest]["temp"])

patients["P003"]["temp"] = 100.4

print("Updated P003:", patients["P003"])

#3

drone = {
    "altitude": 250,
    "speed": 45,
    "battery": 78,
    "gps": "ACTIVE"
}

drone["wind_speed"] = 12
del drone["gps"]

for key, value in drone.items():
    print(key, ":", value)


#4

stock = {
    "Laptop": 12,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

stock["Laptop"] -= 2
stock["Printer"] = 5

for item in list(stock):
    if stock[item] == 0:
        del stock[item]

print(stock)

#5

text = "python makes coding easy and python makes debugging easier"

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

#6

student = {"name": "Asha", "marks": 92}
print(student["name"])

#7


d = {"a": 1, "b": 2}
d["c"] = 3
print(len(d))

#8

data = {"x": 10, "y": 20}
print(data.get("z", 0))


#9

student = {"name": "Ravi", "marks": 85}
print(student["name"])

#10

d = {"a": 1, "b": 2}

d.update({"c": 3})

print(d)