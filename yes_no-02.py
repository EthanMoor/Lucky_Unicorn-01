
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask user if they have played before
    show_instructions = input("Have you played this game before\n").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")



    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")
