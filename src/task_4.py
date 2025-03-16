'''
    Напишіть консольного бота помічника, який розпізнаватиме команди, 
    що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
'''

from scripts import contacts
from colorama import Fore, Back, Style

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print( Back.LIGHTWHITE_EX + Fore.BLACK + "Welcome to the assistant bot!" + Style.RESET_ALL)
    print('')
    while True:
        user_input = input(Fore.BLUE + 'Enter a command: ' + Style.RESET_ALL)
        cmd, *args = parse_input(user_input)
        
        if cmd == '':
            print(Fore.YELLOW + 'Please enter a command.')
            continue
        
        if cmd in ["close", "exit"]:
            print(Back.LIGHTWHITE_EX + Fore.BLACK + 'Goodbye.' + Style.RESET_ALL)
            break
        elif cmd == 'hello':
            print(Fore.GREEN + 'Hello! I am your assistant, how can I help you?' + Style.RESET_ALL)
        elif cmd == 'add':
            if len(args) < 2:
                print(Fore.RED + "Error: Please provide a name and phone number." + Style.RESET_ALL)
                continue
            *name_parts, phone = args
            name = " ".join(name_parts)
            
            contacts.add(name, phone)
        elif cmd == 'remove':
            if len(args) < 1:
                print(Fore.RED + "Error: Please provide a name." + Style.RESET_ALL)
                continue
            name = " ".join(args)
            
            contacts.remove(name)
        elif cmd == 'update':
            if len(args) < 2:
                print(Fore.RED + "Error: Please provide a name and phone number." + Style.RESET_ALL)
                continue
            *name_parts, phone = args
            
            name = " ".join(name_parts)
            contacts.update(name, phone)
        elif cmd == 'show':
            if len(args) < 1:
                print(Fore.RED + "Error: Please provide a name." + Style.RESET_ALL)
                continue
            name = " ".join(args)
            contacts.show(name)
        elif cmd == 'all':
            contacts.all()
        else:
            print(Fore.YELLOW + 'Unknown command. Please try again.')
        
if __name__ == '__main__':
    main()