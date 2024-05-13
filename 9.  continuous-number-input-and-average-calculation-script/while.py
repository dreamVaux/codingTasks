# Ask the user to enter a number or enter '-1' to stop the program
num = int(input("Enter a number or enter '-1' to stop the program: \n"))
# At the beginning, total sum and count are zero.
total_sum = 0
count = 0
# When the user enters number other than '-1', the program will keep asking for more numbers.
while num != -1:
    # During each iteration, total sum of numbers will be added up and be counted.
    total_sum += num 
    count +=1
    num = int(input("Enter a number or enter '-1' to stop the program: \n"))
# If the user type in '-1' and the count > 0, total sum and average (total sum/ count) will be shown to the user.
if count > 0:
    print("Total sum is {}." .format(total_sum))
    print("Average is {}." .format(total_sum/count))
#  If the user enter nothing but '-1', "You didn't enter anything" will be shown.
else:
    print("You didn't enter anything.")