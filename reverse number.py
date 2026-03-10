n = int(input("enter a number"))
def reverse_number(n):
    rvr= 0
    while n>0:
        digit = n%10
        rvr = rvr*10 + digit
        n = n//10
    return rvr
print(reverse_number(n))
