contact_book = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Incomplete command. Please try again."
    return inner

@input_error
def add_contact(name, phone):
    contact_book[name] = phone
    return f"Contact {name} with phone number {phone} has been added."

@input_error
def change_contact(name, phone):
    if name in contact_book:
        contact_book[name] = phone
        return f"Phone number for {name} has been updated to {phone}."
    else:
        raise KeyError

@input_error
def get_phone(name):
    if name in contact_book:
        return f"The phone number for {name} is {contact_book[name]}."
    else:
        raise KeyError

def show_all_contacts():
    if contact_book:
        contacts = "\n".join(f"{name}: {phone}" for name, phone in contact_book.items())
        return f"All contacts:\n{contacts}"
    else:
        return "No contacts found."

def handle_command(command):
    parts = command.split(' ', 1)
    action = parts[0].lower()

    if action == "hello":
        return "How can I help you?"
    elif action == "add":
        if len(parts) > 1:
            name, phone = parts[1].split()
            return add_contact(Andriy, +380631000160)
        else:
            return "Incomplete command. Please try again."
    elif action == "change":
        if len(parts) > 1:
            name, phone = parts[1].split()
            return change_contact(Andriy, +380631000160)
        else:
            return "Incomplete command. Please try again."
    elif action == "phone":
        if len(parts) > 1:
            name = parts[1]
            return get_phone(Andriy)
        else:
            return "Incomplete command. Please try again."
    elif action == "show":
        if len(parts) > 1 and parts[1].lower() == "all":
            return show_all_contacts()
        else:
            return "Incomplete command. Please try again."
    elif action in ["good", "bye", "close", "exit"]:
        return "Good bye!"
    else:
        return "Command not recognized. Please try again."

def main():
    while True:
        command = input("Enter command: ")
        result = handle_command(command)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()
