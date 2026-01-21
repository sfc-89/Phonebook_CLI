from Phonebook import API as test_api


def phonebook_tests():
    """Tests function"""
    #Tests of {erase} command
    assert test_api.erase_command()
    with open("../Phonebook/contacts_database.json", "r") as contacts_database:
        assert contacts_database.readlines() == []
    assert test_api.erase_command() == "    Your phonebook was successfully erased!"
    assert test_api.contact_database == []

    #Test of {add} command
    assert test_api.add_contact_command(contact_name="Test", contact_number="714324") == ("  "
                                                              "Test with 714324 number was successfully "
                                                              "added to phonebook with id 0."
                                                              )
    assert test_api.add_contact_command(contact_name="Test1", contact_number="111111") == ("  "
                                                              "Test1 with 111111 number was successfully "
                                                              "added to phonebook with id 1."
                                                              )
    assert test_api.add_contact_command(contact_name="Test1", contact_number=None) == ("  "
                                                               "Test1 with None number was successfully "
                                                               "added to phonebook with id 2."
                                                               )
    assert test_api.add_contact_command() == ("  "
                                                               "None with None number was successfully "
                                                               "added to phonebook with id 3."
                                                               )
    #Test of {show} (and check if {add} command works)
    assert(
        "ID: 0; Name: Test; Number: 714324" in test_api.show_command() and
         "ID: 1; Name: Test1; Number: 111111" in test_api.show_command() and
         "ID: 2; Name: Test1; Number: None" in test_api.show_command() and
         "ID: 3; Name: None; Number: None" in test_api.show_command()
    )

    #Test of {delete} command
    assert test_api.delete_contact_command(0) == "   Contact 0 was successfully deleted!"
    assert (
        "ID: 0; Name: Test1; Number: 111111" in test_api.show_command() and
        "ID: 1; Name: Test1; Number: None" in test_api.show_command() and
        "ID: 2; Name: None; Number: None" in test_api.show_command()
    )

    #Test of {search} command:
        #No *key
    assert ("    There is no such key '', type 'help' to "
            "see available keys for 'search' command.") == test_api.search_contact_command()
        #By key *id
    assert "    Contact with id None not found!" == test_api.search_contact_command(key="id")
    assert "   Contact with id 4 not found!" == test_api.search_contact_command(key="id", search_item="4")
    assert (
            "Contact with id 1 found:" in test_api.search_contact_command(key="id", search_item="1") and
            "Test1" in test_api.search_contact_command(key="id", search_item="1") and
            "None" in test_api.search_contact_command(key="id", search_item="1")
            )
        #By key *name and *number
    assert "Found 2 records:" in test_api.search_contact_command(key="name", search_item="Test1")
    assert "Test1" in test_api.search_contact_command(key="name", search_item="Test1")
    assert (
            "Found 1 records:" in test_api.search_contact_command(key="number", search_item="111111") and
            "Test1" in test_api.search_contact_command(key="number", search_item="111111") and
            "111111" in test_api.search_contact_command(key="number", search_item="111111")
    )

    #Test of {update} command
        #Update non-existing *id 'kfk'
    assert test_api.update_contact_command(contact_id="kfk") == "    Contact with id kfk not found!"
        #No values only *id
    assert test_api.update_contact_command(contact_id=1) == "   Contact 1 was successfully updated!"
    assert (
        "Name: None" in test_api.search_contact_command(key="id", search_item="1") and
        "Number: None" in test_api.search_contact_command(key="id", search_item="1") and
        "Contact with id 1 found:" in test_api.search_contact_command(key="id", search_item="1")
    )
        #With *id and *contact_new_name values
    assert test_api.update_contact_command(
        contact_id=2,
        contact_new_name="New_Test_1"
    ) == "   Contact 2 was successfully updated!"
    assert (
            "Name: New_Test_1" in test_api.search_contact_command(key="id", search_item="2") and
            "Number: None" in test_api.search_contact_command(key="id", search_item="2") and
            "Contact with id 2 found:" in test_api.search_contact_command(key="id", search_item="2")
    )
        #With *id, *contact_new_name and *contact_new_number values
    assert test_api.update_contact_command(
        contact_id=0,
        contact_new_name="New_Test_0",
        contact_new_number="0123498765"
    ) == "   Contact 0 was successfully updated!"
    assert (
            "Name: New_Test_0" in test_api.search_contact_command(key="id", search_item="0") and
            "Number: 0123498765" in test_api.search_contact_command(key="id", search_item="0") and
            "Contact with id 0 found:" in test_api.search_contact_command(key="id", search_item="0")
    )

    #Test of no command
    assert (
        "There is no TestCommand command. type 'help' "
        "to see list of available commands." in test_api.no_command(input_command="TestCommand")
    )

    #Test of {help} command
    assert (
        """
    List of availiable commands:
    add *contact_name *contact_number - add a contact with id, name and phone number to the phonebook;
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
    help - show this help message.""" in test_api.help_command()
    )

if __name__ == "__main__":
    phonebook_tests()
