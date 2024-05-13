# TASK 1-1
# Assign the string - "Hello World" to String.
String = "Hello World"
# Create new_string to be added modified characters in the end.
new_string = ""


# Use for loop and enumerate() to modify
# the character of the string by upper() or lower()
# and add modified characters to new_string.
for i, char in enumerate(String):
    if i%2 == 0:
        new_string += char.upper()
    else:
        new_string += char.lower()

# Print new_string - "HeLlO WoRlD"
print(new_string)



# TASK 1-2
# Assign the string - 'I am learning to code' to Sentence.
Sentence = 'I am learning to code'
# Use .split() to seperate each word of Sentence and create a list - Words.
Words = Sentence.split(' ')
# Create new_list to be added modified words in the end.
new_list = []


# Use for loop and enumerate() to modify
# the word of the sentence by lower() or upper()
# and add modified words to new_list by .append().
for index, word in enumerate(Words):
    if index%2 == 0:
        new_list.append(word.lower())
    else:
        new_list.append(word.upper())

# Use .join() to combine words altogether to create a new string - new_sentence.
new_sentence = ' '.join(new_list)
# Print new_sentence - "i AM learning TO code".
print(new_sentence)