from sys import argv # this variable holds the arguments passed
# read WYSS section to understand this = this is an "import" module
#(a.k.a library or package in R)"
script, first, second, third = argv # unpack what is in argv and assign to left

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("You're third variable is:", third)


# Whenever argv is being used, the args must be specified when running the script 
