n = input("enter a number")
def palindrome(n):
    reverse = n[::-1]
    if n==reverse:
        return"palindrome num"
    else:
        return"not palindrome"
result = palindrome(n)
print (result)
