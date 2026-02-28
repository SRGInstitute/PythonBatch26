numbers = [3,5,2,5,1,9,4,6,7,10,12]
#setnumbers = set(numbers)
even =0
odd = 0
for num in numbers:
    if num % 2==0:
        even+=1

    else:
        odd+=1
print(even,"this is even number")
print(odd,"this is odd number")
