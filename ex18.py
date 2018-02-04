# Function like a script with argv

def print_two(*args): # "def" sets a funtion, this one called "printt_two"
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args is pointless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# One argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# No arguments

def print_none():
    print("The emptiness of nothing...")



# Now test each Function

print_two("Orlac", "Wizard")
print_two_again("Orlac", "Wizard")
print_one("Cassowary")
print_none()
