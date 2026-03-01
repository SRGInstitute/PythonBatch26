choice=int(input("enter your choice:1)sum\n 2)sub\n 3)mul \n 4)divide\n 0)Exit"))

A=0
B=0

def add(A,B):
    return(A+B)
def sub(A,B):
    return(A-B)
def mul(A,B):
    return(A*B)
def div(A,B):
    return(A/B)
def takeinput():
    global A
    global B
    A=int(input("Please Enter first number"))
    B=int(input("Please Enter second number"))

while choice!=0:
    match choice:
        case 1:
            takeinput()
            result=add(A,B)
            print(result)
        case 2:
            takeinput()
            result=sub(A,B)
            print(result)
        case 3:
            takeinput()
            result=mul(A,B)
            print(result)
        case 4:
            takeinput()
            result=div(A,B)
            print(result)
        case 0:
            print("exit")
            break
        case _:
            print("wrong choice try again")
    choice=int(input("enter your choice:1)sum\n 2)sub\n 3)mul \n 4)divide\n 0)Exit"))
    


            
            

