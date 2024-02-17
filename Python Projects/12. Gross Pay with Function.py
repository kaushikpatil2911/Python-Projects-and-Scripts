def grossPayFunction(hour,rate):
    hour = float(hour)
    rate = float(rate)
    pay = 0
    if hour > 40:
        pay = round(40*rate + (hour -40)*rate*1.5,2)
    else:
        pay = round(hour*rate,2)    
    print(f"Pay: {pay}")

hour = input("Enter Hours : ")
rate = input("Enter Rate : ")
grossPayFunction(hour,rate)