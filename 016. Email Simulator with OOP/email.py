### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
    # Declare the class variable, with default value, for emails.
    # Initialise the instance variables for emails.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    emails = [
        ("hyperionDev@gmail.com", "Welcome to HyperionDev!",
         "This is the content for you."),
        ("DfE@ukmail.com", "Great work on the bootcamp!", "Keep going."),
        ("Tutor@yahoo.com.uk", "Your excellent marks!", "Good job.")
    ]
    # Create 3 sample emails and add it to the Inbox list.
    for email_address, subject_line, email_content in emails:
        inbox.append(Email(email_address, subject_line, email_content))

def list_emails():
    # Create a function which prints the email’s subject_line,
    # along with a corresponding number.
    for index, email in enumerate(inbox):
        print(f"{index}. {email.subject_line}")

def read_email(index):
    # Create a function which displays a selected email.
    # Once displayed, call the class method to
    # set its 'has_been_read' variable to True.
    email = inbox[index]
    print(f"\nEmail from: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Email content: {email.email_content}")
    email.mark_as_read()
    print("\nEmail marked as read.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
       
    if user_choice == "1":
        # add logic here to read an email
        list_emails()
        index = int(input("\nEnter the index of the email to read: "))
        read_email(index)
        
    elif user_choice == "2":
        # add logic here to view unread emails
        print("Unread emails:")
        for email in inbox:
            if not email.has_been_read:
                print(f"{inbox.index(email)} {email.subject_line }")

    elif user_choice == "3":
        # add logic here to quit appplication
        print("\nExiting application.")
        break

    else:
        print("Oops - incorrect input.")
