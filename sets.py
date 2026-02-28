            #SETS

number= [1,2,3,4,4,5,5,5,5,6,6,7,7,7,7,7]
uniquenumber = set(number)
print(uniquenumber)

#Adding & Removing from sets
#items = set()
#items.add("mobile")
#ems.add("laptop")
#tems.add("Earbuds")
#items.add("charger")
#print("Items Add:",items)
#removing
#remove = set()
#items.remove("neckband")
#items.discard("mobile")
#print("items discard",items)
#print("items Remove",items)

#sets operations[Union,Difference,intersection,Symmetric Difference]
#sets = {1,2,3,4}
#sets2 = {3,5,6,7}
#result = sets.union(sets2)
#print("Union=",result)
#result = sets.difference(sets2)
#print("Difference",result)

#result = sets.intersection(sets2)
#print("intersection",result)

students = {"Rachit","sudesh","kajal","aman","ankit"}
students2 = {"Rachit","Sagar"}
#result = students.union(students2)
result = students.intersection(students2)
print("students both",result)

#symmetric Difference
sets = {1,2,3,4,8}
sets2 = {9,8,3,4,5}
result = sets.symmetric_difference(sets2)
print("Symmetric value",result)
            
