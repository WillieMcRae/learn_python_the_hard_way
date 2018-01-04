from sys import argv # import argv module from sys package

script, filename = argv # set argv

txt = open(filename) # filename has been defined at command line via argv

print(f"Here's your file {filename}:") # normal print with format
print(txt.read()) apply function 'read' to object 'txt'

print("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
