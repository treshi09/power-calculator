base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
    result *= base
print(f"{base} raised to the power of {exponent} is: {result}")