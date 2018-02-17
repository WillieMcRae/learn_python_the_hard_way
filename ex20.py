from sys import argv # Loading modules aka packages

script, input_file = argv # at command line, arg will be input input_file

def print_all(f): # Define a function with one argument, 'f'
    print(f.read()) # Indent for what the function does, in this case 'read'

def rewind(f):
    f.seek(0) # Go to start of file defined as 'f'

def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
