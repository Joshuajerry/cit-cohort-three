temp = input("""What temperature do you want to convert to?
             Enter c for celcis
             Enter f for Fahrenheit
             --->""")

if (temp == "f"):
    cel = float(input("Enter temperature in celsius: "))
    cel = (cel * 9/5)+32
    print("The tempeature is", cel, "degrees fahrenheit")

elif (temp == "c"):
    fah = float(input("Enter temperature in fahrenheit: "))
    fah = (fah - 32) * (5/9)
    print("The tempeature is", fah, "degrees celcius")
    
else:
    print("Enter a valid Temperature scale")

