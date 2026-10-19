def add_contact(contacts):
    """Prompts user for a name and phone number, checking for dublicates."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print(f"Error: '{name}' already exists in the contact book. Dublicate entry prevented.")
        return
    phone = input("Enter phone number: ").strip()
    # Simple validation: ensure phone contains only digits and is a reasonable length
    if not phone.isdigit() or not (7 <= len(phone) <= 15):
        print(f"Error: Invalid phone number. Please enter digits only (7 to 15 digits long).")
        return
    contacts[name] = phone
    print(f"Success: Contact '{name}' added successfully.")
def view_contacts(contacts):
    """Displays all stored contacts or a message if the list is empty."""
    if not contacts:
        print("Your contact list is empty.")
        return
    print("\n-- Contact List ---")
    for name, phone in contacts.items():
        print(f"Name:{name} | Phone:{phone}")
        print("-" * 20)
def  search_contact(contacts):
    """Searches for a contact by name(supports partial matches)."""
    if not contacts:
        print("Your contact list is empty.")
        return
    query = input("Enter name (or part of name) to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    if matches:
        print(f"\n--- Found {len(matches)} match(es) ---")
        for name, phone in matches.items():
            print(f"Name: {name} | Phone: {phone}")
            print("-" * 25)
    else:
        print(f"No contacts found matching'{query}'.")
def delete_contact(contacts):
    """Deletes contact by name if it exist."""
    if not contacts:
        print("Your contact list is empty.")
        return
    name = input("Enter the name of the  contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Success: Contact '{name}' has been deleted.")
    else:
            print(f"Error: Contact'{name}' does not exist.")
def main():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                search_contact(contacts)
            elif choice == 4:
                delete_contact(contacts)
            elif choice == 5:
                print("Existing Conatct Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    
    

                     
