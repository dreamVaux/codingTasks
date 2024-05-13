# Ask the user to enter a sentence
str_manip = input("Enter a sentence:\n")

# Calculate and display the length of the sentence
print(len(str_manip))

# Find the last letter of the sentence
last_letter = str_manip[-1:]
# Replace every occurence of the last letter in the sentence with @
str_manip_replace = str_manip.replace (last_letter, "@")
print(str_manip_replace)

# Print the last three characters of the sentence backward
print(str_manip[-1:-4:-1])

# Create a five-letter word that is made up of the first three characters and the last two characters in the sentence
five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)
