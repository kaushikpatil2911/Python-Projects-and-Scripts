# TODO
print("Welcome to Burger Shop!")
size = input("What size of Burger do you want? M, N or L : ")
add_mushroom = input("Do you want mushroom? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : " )

price = 0

if size == "M":
    price = price + 5
elif size == "N":
    price = price + 8
else:
    price = price + 10

if add_mushroom == "Y":
    if size == "M" or size == "N":
        price = price + 1
    else:
        price = price + 2
    
if extra_cheese == "Y":
    price = price + 1

print(f"Your final bill is: ${price}.")    
    