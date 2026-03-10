def palin(num):
    if num==num[::-1]:
        print("palindrome number")
    else:
        print("not palindrome number")

num=input("enter tha number")
palin(num)