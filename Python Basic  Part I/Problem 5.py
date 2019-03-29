# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.


def print_name(first_name, last_name):
    print(f'{last_name} {first_name}')


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print_name(first_name, last_name)
