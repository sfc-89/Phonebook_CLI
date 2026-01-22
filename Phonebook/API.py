import json

# Open JSON file and read data from him, creates a file if it doesn't exist
FILEPATH = "../Phonebook/contacts_database.json"

try:
    contact_database = json.load(open(FILEPATH))
except json.decoder.JSONDecodeError:
    contact_database = []
except FileNotFoundError:
    contact_database = []
    with open(FILEPATH, "w") as file:
        pass


def update_id_after_delete() -> None:
    """Change id value by order after deletion of contact"""
    update_id_after_delete_iterator = 0
    for contact in contact_database:
        contact["id"] = update_id_after_delete_iterator
        update_id_after_delete_iterator += 1


def save_database_to_file() -> None:
    """Saves contacts database to JSON file"""
    with open(FILEPATH, "a") as database:
        database.truncate(0)
        json.dump(contact_database, database, indent=4)


def show_command() -> str:
    """Execution of {show} command, that outputs the whole contacts database"""
    show_output_string = ""
    try:
        show_command_output = ""
        with open(FILEPATH, "r") as database:
            show_command_output = json.load(database)
        for contact in show_command_output:
            show_output_string += (f"    ID: {contact['id']}; Name: {contact['name']}; "
                                   f"Number: {contact['number']} \n")
        show_output_string = f"\n   {len(contact_database)} contacts found: \n" + show_output_string
        return show_output_string
    except json.decoder.JSONDecodeError:
        return "    Your phonebook is empty!"


def erase_command() -> str:
    """Execution of {erase} command, that erases the whole contacts database in file and in contact_database list"""
    global contact_database
    with open(FILEPATH, "w") as database:
        database.truncate()
    contact_database = []
    return "    Your phonebook was successfully erased!"


def add_contact_command(contact_name: str = None, contact_number: str = None) -> str:
    """Execution of {add} command that adds a new contact and bind a new id to it"""
    contact_database.append({
        "id": contact_database[len(contact_database) - 1]["id"] + 1 if len(contact_database) > 0 else 0,
        "name": contact_name,
        "number": contact_number
    })
    save_database_to_file()
    return (
        f"  {contact_name} with {contact_number} number was successfully added to phonebook with id "
        f"{contact_database[len(contact_database) - 1]['id']}."
    )


def search_contact_command(key: str = "", search_item: str = "None") -> str:
    """Execution of {search} command that searches for a specific contact by key and value"""
    search_id: str | int = search_item
    if key == "id":
        try:
            search_id = int(search_item)
            if search_id < len(contact_database):
                return f"""    Contact with id {contact_database[search_id]['id']} found:
                    Name: {contact_database[search_id]["name"]}
                    Number: {contact_database[search_id]["number"]}
                """
            return f"   Contact with id {search_id} not found!"

        except (TypeError, ValueError):
            return f"    Contact with id {search_id} not found!"

    elif key == "name" or key == "number":
        returned_names_string: str = ""
        returned_names_iterator: int = 0
        if search_item != "":
            for contact in contact_database:
                if str(search_item) in str(contact[key]):
                    returned_names_iterator += 1
                    returned_names_string += (f"    ID: {contact['id']}, Name: {contact['name']}, "
                                              f"Number: {contact['number']}, \n")
        returned_names_string = f"Found {returned_names_iterator} records: \n" + returned_names_string
        return f"    {returned_names_string}"

    else:
        return f"    There is no such key '{key}', type 'help' to see available keys for 'search' command."


def delete_contact_command(contact_id: int) -> str:
    """Execution of {delete} command that deletes a specific contact by id"""
    if len(contact_database) > contact_id >= 0:
        contact_database.pop(contact_id)
    else:
        return f"    Contact with id {contact_id} not found!"

    save_database_to_file()
    update_id_after_delete()
    save_database_to_file()
    return f"   Contact {contact_id} was successfully deleted!"


def update_contact_command(contact_id: int, contact_new_name: str = None, contact_new_number: str = None) -> str:
    """Execution of {update} command that updates a specific contact name and number values"""
    try:
        contact_id = int(contact_id)
        if len(contact_database) > contact_id >= 0:
            contact_database[contact_id]["name"] = contact_new_name
            contact_database[contact_id]["number"] = contact_new_number
            save_database_to_file()
            return f"   Contact {contact_id} was successfully updated!"
        else:
            return f"    Contact with id {contact_id} not found!"

    except (TypeError, ValueError):
        return f"    Contact with id {contact_id} not found!"


def help_command() -> str:
    """Execution of {help} command, that prints out all available commands"""
    return ("""
    List of available commands:
    add *contact_name *contact_number - adds a contact with id, name and phone number to the phonebook;
        add *contact_name - adds a contact with id, name and empty phone number to the phonebook;
        add - adds a empty contact with id.
    search *key(id or name or number) *value - search for a specific contact by key and value;
        by default if *value is None.
    delete *id  - delete a contact from the phonebook by id.
    update *id *new_contact_name *new_contact_number - update a specific contact by id and gives it a new name
        and phone; if *new_contact_number* or *new_contact_name* is empty, their values in None by default.
    show - show the all phonebook contacts.
    erase - erase all phonebook.
    exit - exit application.
    help - show this help message.
    """)


def no_command(input_command: any) -> str:
    """Execution of command, that prints out that there is no such command"""
    return f"   There is no {input_command} command. type 'help' to see list of available commands.'"
