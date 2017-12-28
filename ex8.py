

# Make a formatter, space for 4 vars or strings

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # Fill spaces wih numbers
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "There is",
    "A deadly cassowary",
    "Be wary",
    "Of it."
))
