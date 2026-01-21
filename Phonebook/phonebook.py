
import API as api


def get_command(command: str, *args: any) -> str | None:
    """Transmits the command to the phonebook api and returns the response"""
    try:
        match command:
            case "add": return print(api.add_contact_command
            (
                contact_name=args[1] if len(args) > 1 else None,
                contact_number=args[2] if len(args) > 2 else None
            ))
            case "delete": return print(api.delete_contact_command
            (
                contact_id=int(args[1])
            ))
            case "update": return print(api.update_contact_command
            (
                contact_id=(args[1]),
                contact_new_name=[2] if len(args) > 2 else None,
                contact_new_number=args[3] if len(args) > 3 else None
            ))
            case "show": return print(api.show_command())
            case "erase": return print(api.erase_command())
            case "search": return print(api.search_contact_command
            (
                key=args[1] if len(args) > 1 else None,
                search_item=args[2] if len(args) > 2 else None
            ))
            case "help": return print(api.help_command())
            case "exit": return exit()
    except ValueError:
        return print(f"    Invalid value or key, type 'help' to see available values for '{command}' command.")
    return print(api.no_command(command))


if __name__ == '__main__':
    print("\n\n          //////// PHONEBOOK //////// \n\n")
    while True:
        user_command = input("@: ")
        try:
            splited_command = user_command.split(" ")
            get_command(splited_command[0], *splited_command)
        except IndexError:
            pass