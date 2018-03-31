# For loops

# Make some lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for-loop through a list

for number in the_count:
    print(f"This is count {number}")

# Same

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Mixed lists

for i in change:
    print(f"I got {i}")

# Build lists, starting with an empty oranges

elements = [] # empty list

# Use range function

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # use append function
    elements.append(i)

# Now print them out

for i in elements:
    print(f"Element was: {i}")
