# Phonebook_CLI

**Phonebook_CLI** is my learning project, that allows to create a phonebook database, using simple CLI commands.

## Installation

Use this command to get files of this project:
```bash
git clone https://github.com/sfc-89/Phonebook_CLI.git
``` 

## Usage

Just type one of available command in CLI. \
To see what commands available, type a `help` command:

```commandline
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
```
Result of ach change of contact will be automatically saved to `contact_database.json` file. \
\
This database looks like:
```json
[
    {
        "id": 0,
        "name": "New_Test_0",
        "number": "0123498765"
    },
    {
        "id": 1,
        "name": null,
        "number": null
    },
    {
        "id": 2,
        "name": "New_Test_1",
        "number": null
    }
]
```
## Contributors

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This code is open and free to use.