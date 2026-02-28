n=int(input("enter n"))
count=0
for i in range(2,n+1):
    if n%i==0:
        count+=1
        
if count==1:
    print(n,"is prime number")
else:
    print(n,"not a prime number")


