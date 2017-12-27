# Make some variables

name = 'Zed A. Shaw' # remember python uses = while R uses <-
age = 35 # probably a lie now
height = 74 * 2.54 # cm
weight = round(180 * 0.45) #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Print some formatted strings
print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Acually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# Now the tricky line
total = round(age + height + weight)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
