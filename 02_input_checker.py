# Checks user choice is 'integer', 'text or 'image
def user_choice():

    valid = False
    while not valid:

        response = "File type (integer / text / image): ".lower()

        if response == "text" or response == "t":
            return response

        else:
            print("Please choose a valid file type!")
            print()