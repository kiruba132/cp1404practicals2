"""
emails
Estimate: 30 minutes
Actual: 40 minutes
"""


def main():
    """Main function to handle email and name input and store them in a dictionary."""
    email_dict = {}
    email = input("Email: ").strip()
    while email != "":
        name_from_email = extract_name_from_email(email)
        extracted_name = name_from_email.replace('.', ' ').title()
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
        if confirmation == '' or confirmation == 'y':
            name = extracted_name
        else:
            name = input("Name: ").strip().title()
        email_dict[email] = name
        email = input("Email: ").strip()

    print("\nResults:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extracts a name from an email address by splitting at the '@' symbol and capitalizing the part before the '@'."""
    username = email.split('@')[0]
    return username.title()


main()