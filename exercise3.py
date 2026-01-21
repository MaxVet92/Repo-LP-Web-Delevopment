# import json library
import json
import csv
# open contacts json file
with open("contacts.json", "r") as file:
    contacts = json.load(file)

# save back to json file
def save_file(contacts):
    with open("contacts.json", "w", encoding = "utf-8") as file:
        json.dump(contacts, file, indent = 2, ensure_ascii=False)

# let user view their contacts
def view_contacts(contacts):
    while True:
        try:
            print("\n=== Contact Notebook Menu ===")
            print("1. View all contacts")
            print("2. Go back to menu")
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                sorted_contacts = sorted(contacts["people"], key=lambda x: x["last_name"])
                print(json.dumps(sorted_contacts, indent=2, ensure_ascii=False))
            elif user_choice == 2:
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print(user_choice)
            print("Invalid input. Try again.")

# add people to files
def add_contact(contacts):
    while True:
        try:
            print("\n=== Contact Notebook Menu ===")
            print("1. Add contact")
            print("2. Go back to menu")   
            user_choice = int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                person = {
                "first_name": input("Type the first name: "),
                "last_name" :input("Type the last name: "),
                "phone_number": input("Type the phone number: ")
                }
                contacts["people"].append(person)
                save_file(contacts)
                print(f"You added {person["first_name"]} {person["last_name"]} to your notebook")
            elif user_choice == 2:
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print("Invalid input. Try again")

# delete person from file
def remove_contact(contacts):
    while True:
        print("\n=== Contact Notebook Menu ===")
        print("1. Remove contact")
        print("2. Go back to menu")
        try:
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
                            save_file(contacts)
                    if delete_index == None:
                        print("No contact with this name is in your notebook")
            elif user_choice == 2:
                 return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:        
            print("Invalid input. Try again")

def search_contact(contacts):
    while True:
        print("\n=== Contact Notebook Menu ===")
        print("1. Search contact")
        print("2. Go back to menu")
        try:
            user_choice =  int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                first_name_search = input(f"What is the first name of the person you wish to search?")
                last_name_search = input(f"What is the last name of the person you wish to search?")
                seach_index = None
                for index, person in enumerate(contacts["people"]):
                    if person["first_name"] == first_name_search and person["last_name"] == last_name_search:
                        search_index = index
                        print(json.dumps(contacts["people"][search_index], indent=2, ensure_ascii=False))
                    continue
                if search_index == None:
                    print("You either misspelled the name or this person is not in your contact list.")
            elif user_choice == 2:
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print("Invalid input. Try again")

def edit_contact(contacts):
    while True:
        print("\n=== Contact Notebook Menu ===")
        print("1. Edit contact")
        print("2. Go back to menu")
        try:
            user_choice =  int(input("Which action would you like to do? Select (1/2): "))
            if user_choice == 1:
                first_name_edit = input(f"What is the first name of the person you wish to edit?")
                last_name_edit = input(f"What is the last name of the person you wish to edit?")
                edit_index = None
                for index, person in enumerate(contacts["people"]):
                    if person["first_name"] == first_name_edit and person["last_name"] == last_name_edit:
                        edit_index = index
                        while True:
                            print(f"1. {list(contacts["people"][0].keys())[0]}")
                            print(f"2. {list(contacts["people"][0].keys())[1]}")
                            print(f"3. {list(contacts["people"][0].keys())[2]}")
                            action = int(input(f"What would you like to edit? (1/2/3) "))
                            # Check if user entered number between 1 and 3
                            if 1 <= action <= 3:
                                # Check which of the three numbers the user entered
                                if action == 1:
                                    person["first_name"] == input(f"Type in the new first name: ").strip()
                                elif action == 2:
                                    person["last_name"] == input(f"Type in the new last name: ").strip()
                                elif action == 3:                                        
                                    person["phone_number"] == input(f"Type in the new phone number: ").strip()
                                # Ask the user if they want to continue editting. If not
                                more_editting = input("Do you want to keep editting this contact? Type 'Y' or 'N': ").upper()
                                if more_editting == "N":
                                    break
                            # If user entered invalid input
                            else:
                                print("Invalid input. Try again")
                        # Leave the foor loop 
                        break
                if edit_index == None:
                    print("This contact does not exist in your notebook. ")
                save_file(contacts)
            elif user_choice == 2:
                return
            else:
                print("Invalid input: Please try again. You must type 1 or 2")
        except ValueError:
            print("Invalid input. Please try again")

def export_contactlist(contacts):
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


# Let user choose action
def user_menu():
    while True:
        try:
            print("\n=== Contact Notebook Menu ===")
            print("1. View all contacts")
            print("2. Add new contact")
            print("3. Delete contact")
            print("4. Search contact")
            print("5. Edit contact")
            print("6. Export contact list to csv")
            print("7. Exit")
            user_choice = int(input("Which action would you like to do? Select (1/2/3/4/5/6/7): "))
            if user_choice == 1:
                view_contacts(contacts)
            elif user_choice == 2:
                add_contact(contacts)
            elif user_choice == 3:
                remove_contact(contacts)
            elif user_choice == 4:
                search_contact(contacts)
            elif user_choice == 5:
                edit_contact(contacts)
            elif user_choice == 6:
                export_contactlist(contacts)
            elif user_choice == 7:
                exit()
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    user_menu()
