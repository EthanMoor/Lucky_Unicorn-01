import random

# Main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,10):
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

    # Output
    print("You got a {}. Your balance is "
      "${:.2f}".format(chosen, balance))

print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
print()
