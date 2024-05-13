# Define the string as '*****'
string = "*****"
# Set the for loop for i in range(1, 10) because there are 9 lines in the pattern.
for i in range(1, 10):
# For i < 6, let '*' increase as there are more lines.
    if i < 6:
        print(string[0: i])
# For i >= 6, let '*' decrease gradually for the further line.
    else:
        print(string[0: 10-i])