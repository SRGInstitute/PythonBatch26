numbers=int(input("Enter number"))
factor=[]

for num in range(1,numbers):
    if numbers%num==0:
        factor.append(num)



print("Factors",factor)

if sum(factor) == numbers:
    print("number is perfect")
else:
    print("number is not perfect")


