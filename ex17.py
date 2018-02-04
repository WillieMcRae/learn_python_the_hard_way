# Modules/packages
from sys import argv
from os.path import exists

# Command line
script, from_file, to_file = argv # When running file, specify 2 args

# Script running

print(f"Copying from {from_file} to {to_file}") # Explain what is about to happen

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CRTL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
