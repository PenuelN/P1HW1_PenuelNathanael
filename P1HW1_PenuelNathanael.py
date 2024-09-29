# Nathanael Penuel
# 9/29/2024
# P1HW1 - Mathematical Expressions
# This program calculates exponentiation


print("-----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result} !!")


print("\n-----Addition and Subtraction----")
start_value = int(input("Enter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
subtract_value = int(input("Enter an integer to subtract: "))
final_result = start_value + add_value - subtract_value
print(f"{start_value} + {add_value} - {subtract_value} is equal to {final_result}")
