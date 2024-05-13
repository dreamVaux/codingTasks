# Ask the user to enter three integers (cast the answers into integers in advance for further calculation)
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
int3 = int(input("Enter the third integer: "))

# Print out the sum of all the numbers
print(int1 + int2 + int3)
# Print out the first number minus the second number
print(int1 - int2)
# Print out the third number multiplied by the first number
print(int3 * int1)
# Print out the sum of all three numbers divided by the third number
print((int1 + int2 + int3) / int3)