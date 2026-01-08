# Explicit Type Casting Example
# User converts one data type into another

num1 = "25"                 # String value
num2 = "5"                  # String value

int_num1 = int(num1)        # Convert string to integer
int_num2 = int(num2)

sum_result = int_num1 + int_num2

print("String values:", num1, num2)
print("After conversion:", int_num1, int_num2)
print("Sum:", sum_result)

print("Type of num1:", type(num1))
print("Type of int_num1:", type(int_num1))