# Ask user if they have played before
show_instructions = input("Have you played this game before\n")

# If they say yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")
    
# If they say no, output 'display instructions'
else:
    print("Please answer yes / no")
