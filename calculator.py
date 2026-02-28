while True:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print("1 for addition")
    print("subtract")
    print("division")
    print("multiple")
    print("4 exit")
    calculator=int(input("enter the choice"))
   

    match calculator:
    
        case 1:
            print("result",a+b)

        case 2:
            print("result",a-b)

        case 3:
            print("result",a/b)

        case 4:
            print("result",a*b)

        case _:
            break
            
        
