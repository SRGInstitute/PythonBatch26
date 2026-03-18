n=int(input("enter number"))

for i in range(1,n+1):
    if i%2==1:
        print("#"*i,end=" ")
    else:
        print("*"*i,end=" ")

    print("\n")
    
