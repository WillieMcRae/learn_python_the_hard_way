from sys import argv # Import module/package argv

script, filename = argv # The filename name is the file we want to play with

print(f"We're going to read {filename}.") # Uses filename variable from argv
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input("?") # User input

print("Opening the file...")
target = open(filename, 'r')

print("And finally, we close it.")
target.close
