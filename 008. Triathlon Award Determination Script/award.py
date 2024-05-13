# Create a program that can determine the award a person competing a in triathlon will receive

# Ask the person how many minutes did he/she use in swimming, cycling, and running
swimming = int(input("How many minutes did you use in swimming?"))
cycling = int(input("How many minutes did you use in cycling?"))
running = int(input("How many minutes did you use in running?"))

# Calculate and display the total time that the person used in triathlon
total_time = swimming + cycling + running
print("The total time is {} minutes." .format(total_time))

#  Determine the award the person receive by the time he/she used
if (0<= total_time <=100):
    award = "Provincial colours"
elif (101<= total_time <=105):
    award = "Provincial half colours"
elif (106<= total_time <=110):
    award = "Provincial scroll"
else:
    award = "No award"
print("You have {}." .format(award))
