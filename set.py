
student_info = ("Rahul", 20)
name, age = student_info
subject = ["math", "hindi", "math", "computer", "keyboard"]
unique_subject = set(subject)
student = {
    "Name": name,
    "Age": age,
    "Subject": unique_subject
}
print("Student details")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Subject:", student["Subject"])
