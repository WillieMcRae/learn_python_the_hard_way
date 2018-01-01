# Create a script using argv and input from user

from sys import argv # load argv module

script, first = argv # define what argv will unpack to

print("The argv variable is - ", first)

user_var = input("What is the user_var?")

print(f"The user_var is {user_var}.")
