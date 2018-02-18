# Load sys package
import sys

# Command line - define input encoding
script, input_encoding, error = sys.argv

# Make a function
def main(language_file, encoding, errors):
    line = language_file.readline() # Using a method (readline)

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# Make another function (which is being used in the function above)
def print_line(line, encoding, errors):
    next_lang = line.strip() # Using a method (strip)
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

# Reference the source file
languages = open("languages.txt", encoding="utf-8")


# Run the main function
main(languages, input_encoding, error)
