n = int(input("Enter n: "))
for row in range(1,n):
    for col in range(1,n):
        if row+col == 4:
            print("#",end = "")
        else:
            print("*", end="")
    print("\n")
