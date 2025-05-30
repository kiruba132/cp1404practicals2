MINIMUM_LENGTH = 10

def main():
    """Main function to get the password and print asterisks. """
    password = get_password()
    print_asterisks(password)

def get_password():
    """ Prompt the user to enter a password of at least MINIMUM_LENGTH characters """
    password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password too short! It must be at least {MINIMUM_LENGTH} characters.")
        password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")
    return password

def print_asterisks(password):
    """ Print asterisks corresponding to the length of the password. """
    print('*' * len(password))

main()