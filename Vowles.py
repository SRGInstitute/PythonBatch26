def vowles(text):
    vowles1=[]
    for ch in text:
        if ch in "aeiouAEIOU":
            vowles1.append(ch)
    return vowles1

text=input("enter string")
print(vowles(text))