# Python program to demonstrate loops

# For loop example
print("For Loop Example:")
for i in range(1, 6):
    print("Number:", i)

# Loop with condition
print("\nEven Numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# While loop example
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Infinite loop with break
print("\nBreak Example:")
x = 1
while True:
    print("Value of x:", x)
    if x == 3:
        break
    x += 1

# Continue example
print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print("i:", i)

# Nested loop example
print("\nNested Loop Example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)