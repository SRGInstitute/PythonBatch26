while True:
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")

    choice=int(input())
    match choice:

        case 1:
          a=int(input())
          b=int(input())
          print("Result=",a+b)

        case 2:
          a=int(input())
          b=int(input())
          print("Result=",a-b)
    
        case 3:
          a=int(input())
          b=int(input())
          print("Result=",a*b)

        case 4:
          a=int(input)
          b=int(input())
          if b==0:
            print("division by zero not allowed")
          else:
              print("Result=",a/b)
        case 5:
            print("Exiting calculator...")
            break
        case _:
            print("invalid choice")
