def digits(num):
    multiplyofdigit=1
    while num!=0:
        digit=num%10
        multiplyofdigit=multiplyofdigit*digit
        num=int(num/10)
    return multiplyofdigit

num=int(input("enter num"))
print(digits(num))
    
