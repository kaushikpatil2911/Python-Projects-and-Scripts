# Project 9 - Gross Pay with Exception

# Instructions

# Rewrite Gross Pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

# Example Input

# Enter Hours: 20

# Enter Rate: ten

# Example Output

# Error, please enter numeric input for Rate

hour = (input("Enter Hours : "))

try:
    hour = float(hour)
except ValueError:
    print("Error, please enter numeric input for Hours")
    exit()

rate = (input("Enter Rate : "))

try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input for Rate")
    exit()

if hour < 40:
    pay = round(hour*rate,2)
else:
    overtime = hour - 40
    pay = round(40 * rate + overtime * rate * 1.5,2)


print(f"Pay: {pay}")