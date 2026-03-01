
choice=int(input("enter your choice 1) sum \n 2) sub\n 3)mul \n 4) divide \n 0)exit"))
a=0
b=0

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def takeinput():
    global a
    global b
    a=int(input("enter tha value:-"))
    b=int(input("enter tha value:-"))

while choice!=0:
    match choice:
        case 1:
            takeinput()
            print(add(a,b))
        case 2:
            takeinput()
            print(subtract(a,b))
        case 3:
            takeinput()
            print(multiply(a,b))
        case 4:
            takeinput()
            print(divide(a,b))
        case 0:
            print("exit")
        case _:
            print("wrong choice try again")
    choice=int(input("enter your choice 1) sum \n 2) sub\n 3)mul \n 4) divide \n 0)exit"))
    
    

            



    