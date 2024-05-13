# Ask the user how many students are registering.
how_many_students = int(input("How many students are registering?"))

# Open "reg_form.txt" by using implicit method.
with open('reg_form.txt', 'w+') as file:
    # Create a for loop that runs for the number of students.
    for i in range(how_many_students):
        # Each time the loop runs the program,
        # it asks the user to enter student ID number.
        student_id = input("Enter the student ID number:")
        # Write each of the ID numbers to the text file and
        # include a dotted line after each student ID for attendance register.
        file.write(student_id+"* * * *"+"\n")

    # Move the file pointer to the beginning of the file before reading.
    file.seek(0)
    student_id_list = file.read()
    # Print the content of the file.
    print(f"Student ID list:\n{student_id_list}")
