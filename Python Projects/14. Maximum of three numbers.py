# Instruction

# Define a function which takes three integer number as parameters and returns maximum of them.

# Input

# max_of_three(4,5,3)

# Output

# 5

def max_of_three(n1,n2,n3):
    max = n1
    if n2 > max and n2 > n3:
        print(f"Max is {n2}")
    elif n3 > max and n3 > n2:
        print(f"Max is {n3}")
    else:
        print(f"Max is {n1}")       


n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))   
n3 = int(input("Enter number 3 : "))
max_of_three(n1,n2,n3)      