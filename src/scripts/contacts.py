from colorama import Fore, Back, Style

contacts = {}

def add(name: str, phone: str) -> int:
    contacts[name] = phone
    
    print(Fore.GREEN + f'Contact {name} with phone {contacts[name]} added successfully', Style.RESET_ALL)
    return 0
    
def remove(name: str) -> int:
    if name == '':
        print(Fore.RED + 'Error: Please provide a name.', Style.RESET_ALL)
        return 1
    if name not in contacts:
        print(Fore.RED + f'Error: Contact {name} not found.', Style.RESET_ALL)
        return 1
    contacts.pop(name)
    
    print(Fore.GREEN + f'Contact {name} removed successfully', Style.RESET_ALL)
    return 0
    
def update(name: str, phone: str) -> int:
    if name == '':
        print(Fore.RED + 'Error: Please provide a name.', Style.RESET_ALL)
        return 1
    if name not in contacts:
        print(Fore.RED + f'Error: Contact {name} not found.', Style.RESET_ALL)
        return 1
    contacts[name] = phone
    
    print(Fore.GREEN + f'Contact {name} updated with phone {contacts[name]}', Style.RESET_ALL)
    return 0

def show(name: str) -> int:
    if name == '':
        print(Fore.RED + 'Error: Please provide a name.', Style.RESET_ALL)
        return 1
    if name not in contacts:
        print(Fore.RED + f'Error: Contact {name} not found.', Style.RESET_ALL)
        return 1
    
    print(Fore.GREEN + f'Contact {name}: {contacts[name]} found', Style.RESET_ALL)
    return 0

def all() -> int:
    print(Fore.GREEN + f'List of all contacts', Style.RESET_ALL)
    print('')
    for name, phone in contacts.items():
        print(Back.CYAN + f'{name}:' + Back.RESET +  Fore.GREEN + f'\t{phone}', Style.RESET_ALL)
    print('')
    return 0