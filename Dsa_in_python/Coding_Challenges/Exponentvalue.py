def pow(b,e):
    value=1
    for i in range(e):
        value=value*b
    return value
b=int(input("Enter the value of base:"))
e=int(input("Enter an exponent value:"))
print("The value calculated:",pow(b,e))