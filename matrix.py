n=int(input())

#for row in range(1,n+1):
 #   for col in range(1,row+1):
        #if row>=col:
           # print("*",end=" ")
       # else:
       # print(f"*",end="  ")
#    print("\n")

#for row in range(1,n+1):
 #   for col in range(1,row+1):
  #      print(col,end="  ")
   # print("\n")

#for row in range(1,n):
 #   for col in range(1,n):
  #      if abs(row-col) ==1:
   #         print("*",end="  ")
    #    else:
     #       print("#",end="  ")

  #  print("\n")
#for row in range (1,n):
 #   for col in range(1,n):
  #      if row+col==4:
   #         print("*",end="    ")
    #    else:
     #       print("#",end="  ")
    #print("\n")
#pyramid
#for row in range(1,n+1):
 #   for col in range(n-row):
#        print(" ",end="  ")
#
 #   for k in range(2*row-1):
  #      print("#",end="  ")
   # print("\n")


#for row in range(1,n+1):
 #   for col in range(row-1):
  #      print("",end="  ")
   # for k in range(2*(n-row)+1):
    #    print("*",end="  ")
    #print("\n")
    
for row in range(1,n+1) :
    for col in range(1,n+1):
        if (row==1) or (row==n) or (col==1) or (col==n):
            #if row==1 or col==1:
             print("*",end="  ")

        else:
             print("#",end="  ")
    print("\n")
         





























    
