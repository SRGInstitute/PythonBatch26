def vowels(text):
    vowels=[]
    for ch in text:
        if ch in "aeiouAEIOU":
            vowels.append(ch)
    return vowels
text=input("enter a vowels")
print(vowels(text))
