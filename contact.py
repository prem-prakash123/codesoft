ContactBook={}

def display_contact():
    print("Name\t\tcontact number")
    for key in ContactBook:
        print("{}\t\t{}".format(key,ContactBook.get(key)))

while True:
    choice=int(input("1. Add new contact \n2. Search contact \n3. Display contact \n4.Update contact \n5.Exit\n Enter the choice: "))
    
    if choice == 1:
        name=(input("Enter the contact name: "))
        phone=int(input("Enter the phone number: "))
        ContactBook[name]=phone
    
    elif choice == 2:
        search_name = (input("Enter the contact name: "))
        if search_name in ContactBook:
            print(search_name, "'s contact name is ", ContactBook[search_name])
        else:
            print("name is not found in contact book")
    
    elif choice == 3:
        if not ContactBook:
            print("Empty contact book")
        else:
            display_contact()
    
    elif choice == 4:
        update_name=input("Enter the contact name to be edited: ")
        if update_name in ContactBook:
            phone=input("Enter mobile number: ")
            ContactBook[update_name] = phone
            print("contact update sucessfully")
            display_contact
        else:
            print("Name is not found in contack book")
    elif choice ==5:
        delete_contact=input("Enter the contact to be deleted: ")
        if delete_contact in ContactBook:
            ContactBook.pop(delete_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break



