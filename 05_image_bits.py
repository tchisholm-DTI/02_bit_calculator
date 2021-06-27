
# Checks input is a number more than a given value
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

# Finds # of bits for 24 bit colour
def image_bits():

    # Get width and height ...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # Calculate the number of pixels
    num_pixels = image_width * image_height

    # Calculate # of bits (num pixels x 24)
    num_bits = num_pixels * 24

    # Outputs answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# of bits is {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

# Main routine goes here
image_bits()