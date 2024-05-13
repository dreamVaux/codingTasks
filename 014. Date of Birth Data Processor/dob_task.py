# Open "DOB.txt" by using implicit method through relative path.
with open('DOB.txt', 'r+') as file:

    # Create default lists to store names and birthdates.
    name_list = []
    birthdate_list = []

    # Read each line from the file.
    for line in file:
         # Seperate each line into words
        seperated_str = line.split()

        # Combine first name and surname into a string.
        full_name = " ".join(seperated_str[0:2])
        # Combine birthdate information into one string.
        birthdate = " ".join(seperated_str[2:])

        # Append every name to the list - names.
        name_list.append(full_name)
        # Append every birthdate to the list - birthdates.
        birthdate_list.append(birthdate)

# Print out names.
print("Name")
print("\n".join(name_list))
# Print out birthdates.
print("\nBirthdate")
print("\n".join(birthdate_list))