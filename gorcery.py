Grocery = ['onion', 'tamato', 'pea', 'patato', 'genger',
           'sweet patato', 'garlic', 'chilli', 'cabbage']

available = ["garlic", "genger", "patato"]

# Remove available items
for item in available:
    if item in Grocery:
        Grocery.remove(item)

total = 0
for item in Grocery:
    price = int(input("Enter the price of " + item + ": "))
    total += price

print("Total price of grocery:", total)
