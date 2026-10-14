#1

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

#2

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

#3
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ZeroDivisionError:
    print("Division error")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)
    print("Division Successful")


#4

f = None

try:
    f = open("sample.txt", "w")
    f.write("Python File Handling")
    print("File Written Successfully")

except OSError:
    print("File Error")

finally:
    if f is not None:
        f.close()
    print("File Operation Completed")


#5


try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))

    print(a / b)

except Exception as e:
    print("Error:", e)

#6

while True:
    try:
        num = int(input("Enter integer: "))
        print("Valid Number:", num)
        break

    except ValueError:
        print("Invalid input. Try again.")


#7

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

#8


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Eligible")

except ValueError as e:
    print("Error:", e)

#9

class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid marks")

    print("Marks:", marks)

except InvalidMarksError as e:
    print("Error:", e)

#10

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance")

    if amount <= 0:
        raise ValueError("Invalid Amount")

    balance = balance - amount

    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Error:", e)

#11

try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Division by Zero")


#12

numbers = [10, 20, 30]

try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    index = int(input("Enter index: "))

    try:
        print("Division:", a / b)

    except ZeroDivisionError:
        print("Cannot divide by zero")

    try:
        print("List Element:", numbers[index])

    except IndexError:
        print("Invalid List Index")

except ValueError:
    print("Invalid Input")


#practice question 

#1

class LowBatteryError(Exception):
    pass

try:
    battery = int(input("Enter battery: "))

    if battery < 15:
        raise LowBatteryError("Low Battery!")

    print("Flight Continuing")
    print("Distance:", 20 * 2, "km")

except LowBatteryError as e:
    print("Warning:", e)

#2

class InvalidDosageError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    dosage = float(input("Enter dosage: "))

    if age < 1:
        raise InvalidDosageError("Invalid Age")

    if dosage <= 0 or dosage > 1000:
        raise InvalidDosageError("Invalid Dosage")

    print("Dosage Accepted")

except InvalidDosageError as e:
    print("Error:", e)

except ValueError:
    print("Invalid Numeric Input")

finally:
    print("Validation Completed")

#3

class SuspiciousLoginError(Exception):
    pass

password = "1234"

try:
    for i in range(3):
        entered = input("Enter password: ")

        if entered == password:
            print("Login Successful")
            break

        print("Wrong Password")

        if i == 2:
            raise SuspiciousLoginError("Too Many Failed Attempts")

except SuspiciousLoginError as e:
    print("Warning:", e)

finally:
    print("Login Check Completed")

#4

try:
    temperatures = []

    with open("temperature.txt", "r") as f:
        for line in f:
            temp = float(line.strip())

            if temp < -100:
                raise ValueError("Sensor Fault")

            temperatures.append(temp)

    average = sum(temperatures) / len(temperatures)

    print("Average Temperature:", average)

except FileNotFoundError:
    print("File Not Found")

except ValueError as e:
    print("Invalid Data:", e)

except ZeroDivisionError:
    print("No Temperature Data")

#5

class BlankLabelError(Exception):
    pass

class DigitLabelError(Exception):
    pass

class DuplicateLabelError(Exception):
    pass

labels = ["cat", "dog", "cat", "cat"]
counts = {}
limit = 1

try:
    for label in labels:
        if label.strip() == "":
            raise BlankLabelError("Blank Label")

        for ch in label:
            if ch.isdigit():
                raise DigitLabelError("Label Contains Digit")

        counts[label] = counts.get(label, 0) + 1

        if counts[label] - 1 > limit:
            raise DuplicateLabelError("Too Many Duplicates")

    print("Valid Labels")

except BlankLabelError as e:
    print("Error:", e)

except DigitLabelError as e:
    print("Error:", e)

except DuplicateLabelError as e:
    print("Error:", e)

#6

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Math Error")

finally:
    print("Done")


#7

try:
    num = int("25A")

except ValueError:
    print("Invalid")

else:
    print("Valid")

finally:
    print("Closed")

#8

try:
    data = [1, 2, 3]
    print(data[5])

except IndexError:
    print("Out of Range")

finally:
    print("Execution Complete")

#9

try:
    num = 10 / 0

except ZeroDivisionError:
    print("Division error")

finally:
    print("Completed")

#10

class LowMarksError(Exception):
    pass

marks = 25

if marks < 35:
    raise LowMarksError("Fail")