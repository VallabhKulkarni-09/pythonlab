def add_contact(contacts, name, phone, email):
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact for {name} added successfully!")

def get_contact(contacts, name):
    contact_info = contacts.get(name)
    if contact_info:
        print(f"Contact Information for {name}:")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
    else:
        print(f"{name} not found in contacts.")

contacts = {}

add_contact(contacts, 'Anuj', '123-456-7890', 'anuj@email.com')
add_contact(contacts, 'Arush', '987-654-3210', 'arush@email.com')

get_contact(contacts, 'Anuj')
get_contact(contacts, 'Arush')
get_contact(contacts, 'Avi')  # Not in contacts
