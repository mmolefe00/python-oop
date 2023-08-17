# ===== OOP EMAIL SIMULATOR ===== #

"""
This task demonstrates object orientated programming.
Email objects are created from a sample email list and outputted to the user in a readable menu.
The program gives the user options to view their inbox, filter their inbox and view individual emails.
"""

# === EMAIL CLASS === #
# Create class, constructor and methods to create a new Email object.
class Email:

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content, has_been_read=False):

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = has_been_read

    # formatted email output
    def __str__(self):
        underline = '--------------------------------------------------------------------'
        email_output = f'''
From:\t\t{self.email_address}
Subject:\t{self.subject_line}\n\n{self.email_content}
{underline}'''
        return email_output

    # change 'has_been_read' emails from False to True.
    def mark_as_read(self):         # method
        self.has_been_read = True


# === LISTS & SAMPLES === #
# Empty list to store the email objects.
inbox = []

# Sample emails for adding to 'Inbox' list.
email1 = ['elon@tesla.com', 'Terribly Tense Topic', 'Things people say about terribly tense topics!']
email2 = ['jeff@amazon.com', 'Super Serious Subject', 'Sentences that sound super serious...']
email3 = ['steve@apple.com', 'Incredibly Important Information', 'Implications about incredibly important information']
email4 = ['warren@buffetfoundation.org', 'Morbidly Meticulous Meeting', 'Meeting  to discuss morbidly meticulous mandates']

# === FUNCTIONS === #
# Build out the required functions for your program.

def populate_inbox(a, b, c):        # a = email address; b = subject line; c = email contents

    new_email = Email(a, b, c)      # create new email object from Email Class with parameters
    inbox.append(new_email)         # append to inbox list

    # return formatted output as a confirmation of added email ==> shown when print(populate_inbox(a,b,c)
    return f"New Email Added to Inbox.\nThere are now {len(inbox)} emails in your Inbox.\n"


def list_emails(list_):
    underline = '--------------------------------------------------------------------'
    print(f'''
{underline}
                      I N B O X  :  [ {len(list_)} ]
{underline}''')
    # loop through parameter list == "inbox"
    # enumerate to track email number; count: default=0
    for count, obj in enumerate(list_):

        # if object has not been read, status is unread
        if not obj.has_been_read:
            status = 'Unread'
        else:
            status = 'Read'

        # format output: use count+1 to output the email numbers starting from 1 instead of 0 (for user readability)
        print(f'{count+1}. [{status}]\tSubject Line: {obj.subject_line}')

    # format output
    print(f'''{underline}\n''')


def view_unread(list_):
    underline = '--------------------------------------------------------------------'
    print(f'''
{underline}
                        U N R E A D  :
{underline}''')
    # loop through parameter list == "inbox"
    # enumerate to track email number; count: default=0
    for count, obj in enumerate(list_):

        # if object has not been read, status is unread
        if not obj.has_been_read:
            # format output: use count+1 to output the email numbers starting from 1 instead of 0 (for user readability)
            print(f'{count + 1}.\tSubject Line: {obj.subject_line}')

    # format output
    print(f'''{underline}\n''')


def read_email(a):      # a = inbox index value / email number - 1
    # assign variable to selected email in inbox
    r_email = inbox[a-1]

    # display formatted email for user to view
    underline = '--------------------------------------------------------------------'
    print(f'''
Email: {a}
{underline}{r_email}
Status: Read\n''')

    # mark the email as read
    return r_email.mark_as_read


# ===== EMAIL PROGRAM ===== #

# === GREETING === #
greeting = "\nMoogle Presents: Moo-Mail! Your Safe & Secure, Free Email Service!"
print(greeting)


# === POPULATE INBOX === #

# run populate_inbox function with email samples for later use
populate_inbox(email1[0], email1[1], email1[2])         # inbox[0]
populate_inbox(email2[0], email2[1], email2[2])         # inbox[1]
populate_inbox(email3[0], email3[1], email3[2])         # inbox[2]

# added to be already marked as read in printed inbox
populate_inbox(email4[0], email4[1], email4[2])         # inbox[3]
inbox[3].mark_as_read()


# ===== MAIN MENU ===== #
list_emails(inbox)

while True:     # Loop through main menu to keep requiring user inputs until user quits application

    # format heading & Menu input
    print("\n===== MAIN MENU =====\n")
    user_choice = (input('''Would you like to:
    1. Read an email
    2. View unread emails
    3. Refresh Inbox
    4. Quit application

    Enter selection number: '''))
       
    # READ EMAIL
    if user_choice == '1':    # changed integer inputs to string to avoid ValueError & Try-Except blocks

        # select email number - to be used as a parameter in read_email function
        email_num = int(input("Please select the email number (digit) you'd like to read: "))

        # run read email function
        read_email(email_num)

        # mark email as read in inbox list for "refresh inbox"
        inbox[email_num-1].mark_as_read()

        pass  # return to main menu

        
    # VIEW UNREAD EMAILS
    elif user_choice == '2':

        # unread summary: displays a filtered inbox of only unread email subject lines.
        # Note: I only created a function to include formatting. Am aware it can be done without though.
        view_unread(inbox)

        # check if User would like to View ALl
        while True:
            sub_menu = input('''Would you like to view and mark all unread emails? "Yes" or "No"?\n:''').lower()
            if sub_menu == 'yes':
                # format output
                underlines = '--------------------------------------------------------------------'
                print("\n" + underlines)

                # print unread emails with content
                for email in inbox:
                    if not email.has_been_read:
                        print(email)

                        # automatically mark the email as read.
                        email.mark_as_read()

                # confirm to user that all their emails have been marked as read
                print("\n<<< All emails have been marked as read. >>>\n")
                break

            # if user chooses 'no', break from loop
            elif sub_menu == 'no':
                break

            # if user chooses incorrect input, show error message and re-request input.
            else:
                print("Oops! Please answer 'Yes' or 'No'.\n")

        pass  # return to main menu


    # REFRESH INBOX
    elif user_choice == '3':
        list_emails(inbox)  # run list_emails function to crease formatted inbox
        pass  # return to main menu


    # QUIT APPLICATIONS
    elif user_choice == '4':
        # show farewell message
        print('\nGoodbye! See you soon :D')
        break    # end process


    # INCORRECT MENU INPUT
    else:
        # display error message and re-request input
        print("\nOops! Please enter either 1,2,3 or 4.")

# end
