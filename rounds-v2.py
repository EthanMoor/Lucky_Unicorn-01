import random

# Set balance for testing purposes
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
