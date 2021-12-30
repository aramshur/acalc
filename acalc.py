import math
print("Operations:  Add: +    Subtract: -     Multiply: *     Divide: /   Exponent: ^     Square Root: sqrt")
while(True):
    operation=input("Operation: ")
    if(operation=="+"):
        x=float(input(": "))
        y=float(input(": "))
        print(x+y)
    elif(operation=="-"):
        x=float(input(": "))
        y=float(input(": "))
        print(x-y)
    elif(operation=="*"):
        x=float(input(": "))
        y=float(input(": "))
        print(x*y)
    elif(operation=="/"):
        x=float(input(": "))
        y=float(input(": "))
        print(x/y)
    elif(operation=="^"):
        x=float(input(": "))
        y=float(input(": "))
        print(x**y)
    elif(operation=="sqrt"):
        x=float(input(": "))
        print(math.sqrt(x))
    else:
        exit()
