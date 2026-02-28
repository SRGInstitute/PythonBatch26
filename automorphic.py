num=int(input("enter number"))
square=num*num

temp=num

while temp!=0:
    if temp%10==square%10:
        temp=temp//10
        square=square//10
    else:
        print("not a automorphic number")
        break
else:
    print("automorphic number")
