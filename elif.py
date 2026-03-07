
numbers = [20, 30, 60, 50, 70, 6, 9]

smallest = float("infinity")
second_smallest = float("infinity")

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

print(smallest)
print(second_smallest)
