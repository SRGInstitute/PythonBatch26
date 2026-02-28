#for i in range(1,101):
 #   if 1%3==0 or i%5==0 or i%9==0:
  #      print(i
#month = 1
#match month :
 #   case 1|2|3|10|11|12:
  #      print("winter season")
   # case 4|5|6:
      #  print("summer season")
 #   case 7|8|9:
      #  print("rainy season")
a = []
b = []
c = []
for i in range(1,101):
    if i%5==0:
        a.append(i)
    elif i%7==0:
        b.append(i)
    elif i%9==0:
        c.append(i)
        
print(a)
print(b)
print(c)
    
