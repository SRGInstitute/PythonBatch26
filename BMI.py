weight=float(input("enter your weight"))
hieght=float(input("enter your hieght"))

def BMI():
    BMI=weight/(hieght**2)
    return BMI

print(BMI())
