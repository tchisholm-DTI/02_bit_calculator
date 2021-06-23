# Checks input is a number more than zero
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than zero" "or (equal to) {}" .format(low)

        try:

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# Main routine goes here
keep_going = ""
while keep_going == "":
    print()

    # Ask user for an integer (must be more than or equal to 0)
    var_integer = num_check("Enter an integer:", 0) 

    # Ask user for the width and height of an image 
    # (must be greater than or equal to 1
    image_width = num_check("Image Width?:", 1)
    print()
    image_height = num_check("Image Height?:", 1)