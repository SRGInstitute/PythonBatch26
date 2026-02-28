number=int(input("enter number"))

sumofdigit=0

while number!=0:
    digit=number%10
    sumofdigit=sumofdigit+digit
    number=int(number/10)

print(sumofdigit)
