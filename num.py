def number(n):
    sum=0
    while n!=0:
        digit=n%10
        sum=sum*digit
        n=int(n/10)
        
num=int(input("enter tha value"))
result=number(num)
print(result)