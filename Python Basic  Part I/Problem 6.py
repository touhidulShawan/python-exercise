# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

get_numbers = input("Enter some values: ")
list = get_numbers.split(',')
print(f"List: {list}")
print(f"Tuples: {tuple(list)}")
