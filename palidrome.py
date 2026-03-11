def palidrome(n):
    reverse=n[::-1]
    if num==reverse:
        return "palidrome number"
    else:
        return "no palidrome number"

num=input("enter number")
result=palidrome(num)
print(result)
