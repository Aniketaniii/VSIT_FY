#1

for i in range(1, 11):
    if i == 5:
        break
    print(i)


#2

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

#3

for i in range(1, 11):
    if i == 5:
        break
    print(i)


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


#4

numbers = input("Enter numbers: ").split()
search = input("Enter number to search: ")

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Found at position:", i + 1)
        break
else:
    print("Number not found")

#5

n = int(input("Enter number: "))

if n == 0:
    print("Division by zero is not allowed")
else:
    for i in range(1, 101):
        if i % n == 0:
            print("First divisible number:", i)
            break
    else:
        print("No divisible number found")


#6

numbers = input("Enter numbers: ").split()

for x in numbers:
    num = int(x)

    if num < 0:
        continue

    if num > 0:
        print(num)

#7

total = 0

while True:
    num = int(input("Enter number: "))

    if num == 0:
        break

    if num < 0:
        continue

    total = total + num

print("Sum:", total)


#8

password = "1234"
correct = False

for i in range(3):
    entered = input("Enter password: ")

    if entered == password:
        print("Access Granted")
        correct = True
        break
    else:
        print("Wrong Password")

if correct == False:
    print("Access Denied")


#9

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

#10

for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()

#practice question

#1

for row in range(1, 6):
    battery = int(input("Enter battery percentage: "))

    if battery < 15:
        print("Low Battery! Scanning Stopped")
        break

    print("Scanning Row:", row)

#2

cards = [101, 102, 101, 103, 104] * 12
attendance = []

for card in cards:
    if card in attendance:
        continue

    attendance.append(card)
    print("Attendance Marked:", card)

#3

patients = ["Normal", "Normal", "Critical", "Normal"]

for patient in patients:
    if patient == "Critical":
        print("Emergency Detected!")
        break

    print("Patient Checked:", patient)


#4

barcodes = [101, -1, 102, -1, 103]

for code in barcodes:
    if code == -1:
        continue

    print("Scanned Barcode:", code)

#5

correct_pin = "123456"
attempts = 0

while attempts < 5:
    pin = input("Enter 6-digit PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break

    attempts += 1
    print("Wrong PIN")

if attempts == 5:
    print("Account Locked")


#6

temperatures = [24, -1, 26, 28, -2]

total = 0
count = 0

for temp in temperatures:
    if temp < 0:
        continue

    total += temp
    count += 1

if count > 0:
    average = total / count
    print("Average Temperature:", average)
else:
    print("No valid readings")


#7

for section in range(1, 4):
    if section == 3:
        pass
    else:
        print("Section", section, "Checked")


#8

for i in range(1, 101):
    status = int(input("Enter quality (1=Good, 0=Defective): "))

    if status == 0:
        print("Defective Product Found:", i)
        break

    print("Product", i, "Passed")

#9

for day in range(1, 31):
    weekday = (day - 1) % 7

    if weekday == 5 or weekday == 6:
        continue

    print("Day", day, "Traffic Analyzed")

#10

ips = ["10.0.0.1", "192.168.1.8", "192.168.1.8",
       "10.0.0.2", "192.168.1.8"]

suspicious_ip = "192.168.1.8"
count = 0

for ip in ips:
    if ip == suspicious_ip:
        count += 1

        if count == 3:
            print("Intrusion Alert!")
            print("Suspicious IP:", ip)
            break



        
