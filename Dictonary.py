student= { 
    "name":"Ankur",
    "fathersname":"anil kumar",
    "class":"bca",
    "grade":"A",
    "percentage":"79"}

student2= { 
    "name":"Ankush",
    "class":"bca",
    "fathersname":"sumit kumar",
    "grade":"A",
    "percentage":"79"}
studentList = [student]
studentList.append(student2)
for student in studentList:
   #print(student["name"])
   #print(student["fathersname"])
  # print(student["class"])
  # print(student["grade"])
  # print(student["percentage"])
   print(f"student name is {student["name"]}, student fathers name {student["fathersname"]}, student class{student["class"]}, student grades{student["grade"]}")
    #print(student)



