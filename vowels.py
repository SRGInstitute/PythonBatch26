def vowels(text):
    vowels1=[]
    for ch in text:
        if ch in "aeiouAEIOU":
            vowels1.append(ch)
    return vowels1
text = input("enter a string")
print(vowels(text))
        
