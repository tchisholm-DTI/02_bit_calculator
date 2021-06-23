# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}" .format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Main routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Displays instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type

    # For integers, ask for integer
    # (must be an integer more than/equal to 0)

    # For images, ask for width and height
