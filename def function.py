choice = int(input("Enter you choice: 1) Sum \n 2)Sub \n 3) Mul \n 4)Divider \n 0)Exit"))
a = 0
b = 0
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b
def takelnput():
    global a
    global b
    a = int(input("Please Enter first number"))
    b = int(input("Please Enter second number"))
while choice != 0:
    match choice:
        case 1:
            takelnput()
            result = add(a,b)
            print(result)
        case 2:
            takelnput()
            print(sub(a,b))
        case 3:
            takelnput()
            print(mul(a,b))
        case 4:
            takelnput()
            print(div(a,b))
        case 0:
            print("Exit")
            break
        case _:
            print("Wrong choice try again")

choice = int(input("Enter you choice: 1) Sum \n 2)Sub \n 3) Mul \n 4)Divider \n O)Exit"))    
