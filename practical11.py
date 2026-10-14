#1

f = open("sample.txt", "w")

f.write("Python Programming\n")
f.write("File Handling\n")
f.write("Practical 11\n")

f.close()

print("File Created Successfully")

#2

f = open("sample.txt", "r")

print(f.read(), end="")

f.close()

#3

f = open("sample.txt", "r")

print("Using readline():")
print(f.readline(), end="")

f.seek(0)

print("Using for loop:")
for line in f:
    print(line, end="")

f.close()

#4

with open("sample.txt", "w") as f:
    f.write("Python Programming\n")
    f.write("File Handling\n")
    f.write("Practical 11\n")

with open("sample.txt", "r") as f:
    print(f.read(), end="")


#5

with open("sample.txt", "a") as f:
    f.write("Reading files\n")
    f.write("Writing files\n")

with open("sample.txt", "r") as f:
    print(f.read(), end="")

#6

with open("sample.txt", "r") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))

#7

word = input("Enter word to search: ")

with open("sample.txt", "r") as f:
    text = f.read()

count = text.lower().split().count(word.lower())

print("Occurrences:", count)

#8

with open("sample.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)

with open("copy.txt", "r") as f:
    print(f.read(), end="")

#9

word = input("Enter keyword: ")

with open("sample.txt", "r") as f:
    with open("filtered.txt", "w") as new:
        for line in f:
            if word.lower() in line.lower():
                new.write(line)

with open("filtered.txt", "r") as f:
    print(f.read(), end="")

#10

with open("students.txt", "w") as f:
    f.write("101,Rahul,85\n")
    f.write("102,Amit,90\n")
    f.write("103,Neha,95\n")

with open("students.txt", "r") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        print("Roll:", roll, "Name:", name, "Marks:", marks)


#11

try:
    f = open("missing_file.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("Error: File not found")


#12

with open("sample.txt", "r") as f:
    text = f.read()

text = text.replace("Python", "Java")

with open("sample.txt", "w") as f:
    f.write(text)

print("File Updated Successfully")

with open("sample.txt", "r") as f:
    print(f.read(), end="")

#practice question 

#1

logs = [
    "ALT=250,SPD=45,BAT=78",
    "ALT=260,SPD=50,BAT=65",
    "ALT=270,SPD=55,BAT=48",
    "ALT=280,SPD=60,BAT=40",
    "ALT=290,SPD=55,BAT=35"
]

with open("flight_log.txt", "a") as f:
    for log in logs:
        f.write(log + "\n")

count = 0

with open("flight_log.txt", "r") as f:
    for line in f:
        print(line, end="")
        battery = int(line.strip().split("BAT=")[1])

        if battery < 50:
            count += 1

print("Low Battery Entries:", count)

#2

with open("patient_notes.txt", "w") as f:
    f.write("P001: Stable\n")
    f.write("P002: critical fever\n")
    f.write("P003: Normal\n")
    f.write("P004: critical injury\n")
    f.write("P005: Recovering\n")

with open("patient_notes.txt", "r") as f:
    for line in f:
        if "critical" in line.lower():
            print(line, end="")


#3

with open("audit_log.txt", "a") as f:
    f.write("user=admin,status=FAILED\n")
    f.write("user=asha,status=SUCCESS\n")
    f.write("user=ravi,status=FAILED\n")
    f.write("user=guest,status=FAILED\n")

count = 0

with open("audit_log.txt", "r") as f:
    with open("threat_log.txt", "w") as new:
        for line in f:
            if "status=FAILED" in line:
                count += 1
                new.write(line)

print("Failed Logins:", count)

with open("threat_log.txt", "r") as f:
    print(f.read(), end="")

#4

prompts = [
    "Explain Python loops",
    "Summarize machine learning",
    "Describe neural networks",
    "Explain file handling",
    "Generate practice questions",
    "Analyze student scores",
    "Describe cloud computing",
    "Compare sorting algorithms",
    "Explain data privacy",
    "Summarize research paper"
]

with open("prompt_bank.txt", "w") as f:
    for prompt in prompts:
        f.write(prompt + "\n\n")

cleaned = []

with open("prompt_bank.txt", "r") as f:
    for line in f:
        if line.strip():
            cleaned.append(line.strip())

with open("prompt_bank.txt", "w") as f:
    for prompt in cleaned:
        f.write(prompt + "\n")

total = 0

for prompt in cleaned:
    total += len(prompt.split())

average = total / len(cleaned)

print("Total Prompts:", len(cleaned))
print("Average Words:", average)


#5

records = [
    "TEMP=32,HUM=70,WIND=15",
    "TEMP=34,HUM=68,WIND=12",
    "TEMP=31,HUM=75,WIND=10",
    "TEMP=36,HUM=65,WIND=18",
    "TEMP=33,HUM=72,WIND=14",
    "TEMP=35,HUM=67,WIND=16",
    "TEMP=30,HUM=80,WIND=11"
]

with open("weather.txt", "w") as f:
    for record in records:
        f.write(record + "\n")

highest = 0
highest_day = 0
day = 0

with open("weather.txt", "r") as f:
    for line in f:
        day += 1
        print("Day", day, ":", line.strip())

        temp = int(line.split(",")[0].split("=")[1])

        if temp > highest:
            highest = temp
            highest_day = day

print("Highest Temperature:", highest)
print("Highest Temperature Day:", highest_day)

#6

try:
    with open("demo.txt", "w") as f:
        f.write("Python\nAI")

    with open("demo.txt", "r") as f:
        print(f.readline().strip())

finally:
    print("Done")


#7

with open("demo.txt", "w") as f:
    f.write("A\nB\nC")

with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))

#8

with open("demo.txt", "w") as f:
    f.write("DATA")

with open("demo.txt", "a") as f:
    f.write("SCIENCE")

with open("demo.txt", "r") as f:
    print(f.read())


#9

with open("report.txt", "w") as f:
    f.write("Python Lab\n")
    f.write("Practical 11")

print("File Created")

#10

with open("audit_log.txt", "r") as f:
    for line in f:
        if "FAILED" in line:
            print(line.strip())
        else:
            pass




        