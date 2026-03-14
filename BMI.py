height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))
def BMI(height,weight):
    BMI = weight/(height**2)
    return BMI
print("your body mass index is",BMI(height,weight))
