#1

text = "Programming"

print("First Character:", text[0])
print("Last Character:", text[-1])
print("Middle Character:", text[len(text)//2])

#2

text = "Programming"

print("First 5:", text[:5])
print("Last 4:", text[-4:])
print("Index 2 to 7:", text[2:7])

#3

text = "Python"

print("Alternate:", text[::2])
print("Reverse:", text[::-1])

#4

text = "Python"

# text[0] = "J"  # TypeError

text = "J" + text[1:]

print(text)

#5

text = "Python Programming"

if "Python" in text:
    print("Python Found")

if "Java" not in text:
    print("Java Not Found")

#6

text = "Python Programming"

print("Find:", text.find("Programming"))
print("Index:", text.index("Programming"))
print("Not Found:", text.find("Java"))

# 7

text = "banana banana"

print("Count of a:", text.count("a"))
print("Count of banana:", text.count("banana"))

#8

text = "pYtHon programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())

#9

text = "  Python is easy  "

text = text.strip()
text = text.replace("Python", "Java")

print("Updated:", text)
print(f"Formatted: {text}")

#10

text = "Python makes coding easy"

words = text.split()
joined = "-".join(words)

print("Split:", words)
print("Joined:", joined)

#11

text = input("Enter word: ")

text = text.lower()
reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#12

text = input("Enter paragraph: ")

words = text.lower().split()

print("Word Count:", len(words))
print("Character Count:", len(text))

most = ""
highest = 0

for word in words:
    count = words.count(word)

    if count > highest:
        highest = count
        most = word

print("Most Frequent Word:", most)
print("Frequency:", highest)



#practice question 
#1

text = " Python makes NLP powerful "

text = text.strip()
text = text.lower()

words = text.split()
result = "_".join(words)

print("Words:", words)
print("Result:", result)


#2

student_id = "STU2026CS1098"

print("First 4:", student_id[:4])
print("Last 4:", student_id[-4:])

masked = student_id[:4] + "****" + student_id[-4:]

print("Masked ID:", masked)

#3

log = "ALT:250|SPD:45|BAT:78"

parts = log.split("|")

altitude = parts[0].split(":")[1]
speed = parts[1].split(":")[1]
battery = parts[2].split(":")[1]

print("Altitude:", altitude)
print("Speed:", speed)
print("Battery:", battery)

#4


password = "PySecure2026!"

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digit:", digit)
print("Special Character:", special)
print("Minimum Length:", len(password) >= 8)

if upper and lower and digit and special and len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")



#5

text = "fever cough fever fatigue fever cold"

words = text.split()
unique = []

for word in words:
    if word not in unique:
        unique.append(word)

most = ""
highest = 0

for word in unique:
    if words.count(word) > highest:
        highest = words.count(word)
        most = word

print("Fever Count:", words.count("fever"))
print("Unique Symptoms:", unique)
print("Most Repeated:", most)

#6

text = "PythonProgramming"
print(text[2:10:2])


#7

s = " Data Science "
print(s.strip().upper().replace(" ", "_"))


#8

msg = "AI|ML|DL|NLP"

parts = msg.split("|")

print("-".join(parts[::-1]))


#9
text = "PythonProgramming"
print(text[6:])


#10

sentence = "Python makes coding easy"
print(sentence.replace(" ", "-"))




