from sys import argv # Import module/package argv

script, filename = argv # The filename name is the file we want to play with

print(f"We're going to erase {filename}.") # Uses filename variable from argv
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input("?") # User input

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n") # New line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close
