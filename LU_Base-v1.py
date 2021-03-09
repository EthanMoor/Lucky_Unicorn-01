import random

# Functions go here...


def yes_no(question):
    statement_generator("Welcome to the Lucky Unicorn Game", "*")
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
    statement_generator("How To Play", "*")
    print()
    print("Choose a starting amount (minimum $1 and maximum $10\n"
          "Then Press <Enter> to play. You will get either a Unicorn, Donkey, Horse or a Zebra\n"
          "It will cost $1 per round. Depending on your prize you could win some of your money back\n"
          "Here's the payout amounts:\n"
          "Unicorn = $5 (Balance increases by $4)\n"
          "Horse = -$0.50 (Balance decreases by $0.50)\n"
          "Zebra = -$0.50 (Balance decreases by $0.50\n"
          "Donkey = -$1.00 (Balance decreases by $1.00)")
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


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""




played_before = yes_no("Have you played this game before?\n")

if played_before == "no":
    instructions()

# Ask user how much they want to play with
statement_generator("Lets get started", "-")
how_much = num_check("How much would you "
                     "like to play with? \n"
                     "$", 0, 10)

balance = how_much

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
        chosen = statement_generator("You got a Unicorn", "!")

        balance += 4

    # If the random # is between 6 and 36 #  User gets a Donkey (Subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = statement_generator("You got a Donkey", "D")
        balance -= 1

    else:
        # If the number is either a horse or zebra, in both cases, subtract $0.50 from the balance
        if chosen_num % 2 == 0:
            chosen = statement_generator("You got a Horse", "H")

        else:
            chosen = statement_generator("You got a Zebra", "Z")
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
statement_generator("Results", "=")
print("Final Balance $",balance)
