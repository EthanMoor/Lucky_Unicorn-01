import random

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
                response = "yes"
                return response

        elif response == "no" or response == "n":
                response = "no"
                return response

        else:
            print("Please answer yes / no")


def instructions():
    print("--- How to Play ---")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)
# Main Routine goes here...


played_before = yes_no("Have you played this game before?\n")

if played_before == "no":
    instructions()

# Ask user how much they want to play with
how_much = num_check("How much would you "
                     "like to play with? \n"
                     "$", 0, 10)

balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust Balance
    # If the random # is between 1 and 6 User gets a Unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # If the random # is between 6 and 36 #  User gets a Donkey (Subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    else:
        # If the number is either a horse or zebra, in both cases, subtract $0.50 from the balance
        if chosen_num % 2 == 0:
            chosen = "horse"

        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is "
          "${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                       "or 'xxx to quit\n")

print()
print("Final Balance", balance)
