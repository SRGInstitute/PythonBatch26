from datetime import datetime

currentHour=datetime.now().hour
currentMinute=datetime.now().minute
currentSecond=datetime.now().second

name=input("Enter Name: ")

def  greetuser(name):
    currentHour=datetime.now().hour
    currentMinute=datetime.now().minute
    currentSecond=datetime.now().second
    if currentHour<12:
        return "good morning " + name
    elif currentHour<16:
        return "good afternoon " + name
    elif currentHour<20:
        return "good evening " + name
    else:
        return "good night " + name

print(greetuser(name))
        
    
