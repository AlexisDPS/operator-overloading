# Group 10
# Broden Black
# Alexis De Paz Salazar
# Lab Assignment 6 - A program that allows the user to view, search, and modify a contact list made up of
# contact objects. A contact has a name, phone number, address, city, and zip code. Contacts are
# initially read in from the file ‘addresses.txt’ and then are written back to the file when the
# program ends.

import contact
import check_input


def read_file():
    """open the file, read in each contact (one per line), 
    construct a Contact object using the data, 
    and then store the Contact object in the list of contacts. 
    Sort and then return the filled list."""

    file = open("addresses.txt")
    lines = file.readlines()
    new_contacts = []

    for line in lines:  # Goes through file lines adding contacts
        data = line.strip().split(",")
        new_contacts.append(contact.Contact(data[0], data[1], data[2], data[3], data[4], data[5]))

    new_contacts.sort() # Sorts the contacts
    return new_contacts
        

def write_file(contacts):
    # passes in the list of contacts. Open the file for writing, loop through the contacts list and write each contact to the file using the repr method. Write each contact on a new line
    with open("addresses.txt", "w") as file:
        for contact_item in contacts:
            file.write(repr(contact_item) + "\n")

def get_menu_choice():
    # display the main menu to the user and then take in and return the user’s valid input
    print("Roladex Menu: ")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Save and Quit")
    input1 = check_input.get_int_range("> ", 1, 5)
    return input1

def modify_contact(mod_contact):
    # pass in a contact object. In a loop, display the modify menu to the user, get the user’s valid input, then, based on the user’s choice, prompt the user for the information they’d like to change, and then update the appropriate attribute for the contact. 
    # The user may repeatedly change any of the contact’s values until they choose option 7 to end the loop. The list may need to be resorted after modifications are made.
    menu_change = True

    while menu_change:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")
        
        choice = check_input.get_int_range("> ", 1, 7)
        
        if choice == 1:
            mod_contact.first_name = input("First name: ")

        elif choice == 2:
            mod_contact.last_name = input("Last name: ")

        elif choice == 3:
            mod_contact.phone = input("Phone #: ")

        elif choice == 4:
            mod_contact.address = input("Address: ")

        elif choice == 5:
            mod_contact.city = input("City: ")

        elif choice == 6:
            mod_contact.zip = input("Zip: ")

        elif choice == 7:
            menu_change = False
                

            

def main():
    contacts = read_file()

    get_choice = True

    while get_choice:
        choice = get_menu_choice()

        if choice == 1:
            print("Number of contacts:", len(contacts))
            contact_num = 1
            for cont in contacts:
                print(str(contact_num) + ". " + str(cont))
                contact_num += 1
        elif choice == 2:
            print("Enter new contact:")
            name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone number: ")
            address = input("Address: ")
            city = input("City: ")
            zip_code = input("Zip: ")

            new_contact = contact.Contact(name, last_name, phone, address, city, zip_code)
            contacts.append(new_contact)
            contacts.sort()

        elif choice == 3:
            print("Search:")
            print("1. Search by last name")
            print("2. Search by zip")

            choice = check_input.get_int_range("> ", 1, 2)
            
            if choice == 1:
                search = input("Enter last name: ")

                for contact_item in contacts:
                    if contact_item.last_name == search:
                        print(contact_item)
            else:
                search = input("Enter zip code: ")

                for contact_item in contacts:
                    if contact_item.zip == search:
                        print(contact_item)

        elif choice == 4:
            first_name = input("First name: ")
            last_name = input("Last name: ")
            for contact_item in contacts:
                if contact_item.first_name == first_name and contact_item.last_name == last_name:
                    print(contact_item)
                    modify_contact(contact_item)
                    contacts.sort()

        elif choice == 5:
            print("Saving File...")
            write_file(contacts)
            print("Ending program")
            get_choice = False
    read_file()

main()