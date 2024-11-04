contact = {}


def add_contact():
    if user == "1":
        user_name = input("Enter your contact name: ")
        if user_name in contact:
            print('The name is already exist please try again')
            return

        else:
            print(f'You successfully add {user_name}')
            user_num = int(input("Enter your phone number"))
            contact[user_name] = user_num


def view_contacts():
    if user == "2":
        if not contact:
            print("there is no contact")

        else:
            print(contact)
def search_contacts():
    if user == "3":
        user_search = input("Enter the contact name you want to search: ")
        if user_search not in contact:
            print("Sorry there were no one")

        else:
            print(f'here is hime {contact}')
while True:
    user = input("1:Adding a new contact\n"
                 "2:Viewing all contacts\n"
                 "3:Searching for a specific contact\n"
                 "4:Exiting the program: ")

    if user == "1":
        add_contact()

    elif user == "2":
        view_contacts()

    elif user == "3":
        search_contacts()

    elif user == '4':
        print('Thank you for using')
        break