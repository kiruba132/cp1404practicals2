MINIMUM_LENGTH = 10

def get_password():
    password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password too short! It must be at least {MINIMUM_LENGTH} characters.")
        password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")
    print('*' * len(password))

get_password()