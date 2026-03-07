def factorial(n):
    factor=1
    for i in range(1,n+1):
        factor=factor*i
    return factor
num=int(input("enter tha value"))
result=factorial(num)
print("factorial",result)
