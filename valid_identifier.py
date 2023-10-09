#Importing re to provide regular expression support
import re

def check_valid_identifier(identifier):
    # Here we define a regular expression pattern for a valid identifier

    # The first character is either a lowercase character(a-z), an uppercase character(A-Z) or an underscore(_)
    # It can be followed by zero or more letters (uppercase or lowercase), digits, or underscores.
    # It should not contain any other characters, such as spaces or special symbols.

    pattern = '^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    # Here, we use the re.match() function to check if the identifier matches the pattern
    if re.match(pattern, identifier):
        return True
    else:
        return False
    

# Input identifier to be tested
input_identifier = input("Enter an identifier: ")

if check_valid_identifier(input_identifier):
    print(f"{input_identifier} is a valid identifier.")
else:
    print(f"{input_identifier} is not a valid identifier.")
