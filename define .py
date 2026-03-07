#define triangle
a=int(input("Enter a first side:"))
b=int(input("Enter a second side:"))
c=int(input("Enter a third side:"))
if(a==b==c):
    print("this is equilateral triangle")
elif a==b or b==c or c==a:
    print("this is isolaces triangle")
else:
    print("this scaler triangle") 
