
def save_file_to_json(contacts: dict):
    # save back to json file
    with open("contacts.json", "w", encoding = "utf-8") as file:
        json.dump(contacts, file, indent = 2, ensure_ascii=False)

def menu_choice() -> int:
    # This is the main menu
    # Ask the user what they would like to do next 
    # Save the response in the variable user_choice
    print("\n=== Contact Notebook Menu ===")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Edit contact")
    print("6. Export contact list to csv")
    print("7. Exit")
    user_choice = int(input("Which action would you like to do? Select (1/2/3/4/5/6/7): "))
    return user_choice

def second_level_menu(user_choice: int):
    # This is the menu in the second level, once the user selected an option
    print("\n=== Contact Notebook Menu ===")
    if user_choice == 1:
        print("1. View all contacts")
    elif user_choice == 2:
        print("1. Add contact")
    elif user_choice == 3:
        print("1. Remove contact")
    elif user_choice == 4:
        print("1. Search contact")
    elif user_choice == 5:
        print("1. Edit contact")
    print("2. Go back to menu")

def view_contactlist(contacts: dict, main_choice: int):
    # let user view their contacts
    while True:
        try:
            second_level_menu(main_choice)
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                sorted_contacts = sorted(contacts["people"], key=lambda x: x["last_name"])
                print(json.dumps(sorted_contacts, indent=2, ensure_ascii=False))
            elif user_choice == 2:
                return
        except ValueError:
            print(user_choice)
            print("Invalid input. Try again.")

def contact_details_of_person_to_add() -> dict:
    person = {
                "first_name": input("Type the first name: "),
                "last_name" :input("Type the last name: "),
                "phone_number": input("Type the phone number: ")
                }
    return person
 
def add_contact_to_notebook(contacts: dict, main_choice: int):
    # Let the user add a contact to their notebook
    while True:
        try:
            second_level_menu(main_choice)
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                person = contact_details_of_person_to_add()
                contacts["people"].append(person)
                save_file_to_json(contacts)
                print(f"You added {person["first_name"]} {person["last_name"]} to your notebook")
            elif user_choice == 2:
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print("Invalid input. Try again")

def remove_specific_contact(contacts: dict, main_choice: int):
    # Let the user delete a contact
    while True:
        try:
            second_level_menu(main_choice)
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                    first_name_delete = input(f"What is the first name of the person you wish to remove?")
                    last_name_delete = input(f"What is the last name of the person you wish to remove?")
                    delete_index = None
                    for index, person in enumerate(contacts["people"]):
                        if person["first_name"] == first_name_delete and person["last_name"] == last_name_delete:
                            delete_index = index
                            contacts["people"].pop(delete_index)
                            print(f"You deleted {first_name_delete} {last_name_delete} from your notebook")
                            save_file_to_json(contacts)
                    if delete_index == None:
                        print("No contact with this name is in your notebook")
            elif user_choice == 2:
                 return
        except ValueError:        
            print("Invalid input. Try again")

def search_specific_contact(contacts: dict, main_choice: int):
    # Let the user search for contacts
    while True:
        try:
            second_level_menu(main_choice)
            user_choice =  int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                first_name_search = input(f"What is the first name of the person you wish to search?")
                last_name_search = input(f"What is the last name of the person you wish to search?")
                search_index = None
                for index, person in enumerate(contacts["people"]):
                    if person["first_name"] == first_name_search and person["last_name"] == last_name_search:
                        search_index = index
                        print(json.dumps(contacts["people"][search_index], indent=2, ensure_ascii=False))
                    continue
                if search_index == None:
                    print("You either misspelled the name or this person is not in your contact list.")
            elif user_choice == 2:
                return
        except ValueError:
            print("Invalid input. Try again")

def apply_edit(person: dict, action: int):
    # Overwrite the contactlist based on user input for editting
    if action == 1:
        person["first_name"] = input("Type in the new first name: ").strip()
    elif action == 2:
        person["last_name"] = input("Type in the new last name: ").strip()
    elif action == 3:
        person["phone_number"] = input("Type in the new phone number: ").strip()
    else:
        print("Invalid input. Try again")

def edit_menu():
    # functions regardimng contact editting
    print("1. first_name")
    print("2. last_name")
    print("3. phone_number")

def find_contact(contacts, first_name: str, last_name: str):
    # Find contact for editting
    for person in contacts["people"]:
        if person["first_name"] == first_name and person["last_name"] == last_name:
            return person
    return None

def edit_contact_fields(person: dict):
    # Helper: edit multiple fields of a single contact
    while True:
        edit_menu()
        try:
            action = int(input("What would you like to edit? (1/2/3): "))
            if 1 <= action <= 3:
                apply_edit(person, action)
                more_editing = input(
                    "Do you want to keep editing this contact? Type 'Y' or 'N': "
                ).upper()
                if more_editing == "N":
                    break
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Try again")

def edit_specific_contact(contacts: dict, main_choice: int):
    # Main function to edit contacts
    while True:
        # Show the second-level menu based on the main choice (Edit contact)
        second_level_menu(main_choice)
        try:
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                # Ask which contact to edit
                first_name = input("What is the first name of the person you wish to edit? ")
                last_name = input("What is the last name of the person you wish to edit? ")
                person = find_contact(contacts, first_name, last_name)
                if person is None:
                    print("This contact does not exist in your notebook.")
                    continue  # back to second-level menu
                # Loop to edit multiple fields if desired
                edit_contact_fields(person)
                # Save after editing
                save_file_to_json(contacts)
                print(f"You successfully edited {first_name} {last_name}")
            elif user_choice == 2:
                # Go back to the main menu
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print("Invalid input. Please try again")

def export_contactlist_to_csv(contacts: dict):
# This lets user export the contact list to a csv
# Load your contacts
    csv_file = "contacts.csv"
    # Write contacts to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["first_name", "last_name", "phone_number"])
        # Write each contact
        for person in contacts["people"]:
            writer.writerow([person["first_name"], person["last_name"], person["phone_number"]])

    print(f"Contacts exported successfully to {csv_file}")

def user_menu():
    # This is the main user guiding menu
    # Depending on the user choice, a different function gets invoked
    while True:
        try:
            # Invoking menu_choice function to acquire user_choice for menu option
            user_choice = menu_choice()
            # Guiding the user to the next menu based on their decision
            if user_choice == 1:
                view_contactlist(contacts, user_choice)
            elif user_choice == 2:
                add_contact_to_notebook(contacts, user_choice)
            elif user_choice == 3:
                remove_specific_contact(contacts, user_choice)
            elif user_choice == 4:
                search_specific_contact(contacts, user_choice)
            elif user_choice == 5:
                edit_specific_contact(contacts, user_choice)
            elif user_choice == 6:
                export_contactlist_to_csv(contacts)
            elif user_choice == 7:
                exit()
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    # import libraries
    import json
    import csv

    with open("contacts.json", "r") as file:
    # open contacts json file
        contacts = json.load(file)

    user_menu()
