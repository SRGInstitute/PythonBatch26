import math
num=int(input("Enter number"))
original=num
temp=num
sum=0
digits=int(math.log10(num))+1


while temp!=0:
    digit=temp%10
    sum=sum+digit**digits
    temp=temp//10

if sum==original:
    print("armstrong number")
else:
    print("not armstrong number")
    
    
