types_of_people = 10
x = f"There are {types_of_people} types of people." # Var in string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}") # string in string
print(f"I also said: '{y}'")

hilarious = False
# Leave 'space' in string for a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Use .format to select variable to be placed in string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
