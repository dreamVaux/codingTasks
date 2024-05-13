# pseudocode
# 1. Ask for Name, Age, House number, and Street name step by step.
# 2. Print out all the information in one sentence.
# This is (Name). He/She is (Age) years old and lives at House Number (House number) on (Street name).

# Ask for Name
Name = input("What is your name?")
# Ask for Age
Age = input("What is your age?")
# Ask for House number
House_number = input("What is your house number?")
# Ask for Street name
Street_name = input("What is your street name?")
# Show all information in one sentence
print("This is {0}. He/She is {1} years old and lives at house number {2} on {3}." .format(Name, Age, House_number, Street_name))
