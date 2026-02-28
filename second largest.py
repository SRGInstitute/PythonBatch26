num=int(input("enter number"))
firstlargest=float("-inf")
secondlargest=float("-inf")
digits=[]

while num!=0:
    digit=num%10
    digits.append(digit)
    num=int(num/10)
print(digits)

for digit in digits:
    if digit>firstlargest:
        secondlargest=firstlargest
        firstlargest=digit
    elif digit>secondlargest:
        secondlargest=digit

print(firstlargest)
print(secondlargest)
        
        
