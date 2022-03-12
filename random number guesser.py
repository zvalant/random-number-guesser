import random
def random_guess():
    attempts = 1
    valid_f = valid_e = valid_v = False
    while valid_f is False:
        range_first = input("Enter the start of the range: ")
        if range_first.isdigit():
            range_first = int(range_first)
            valid_f = True
        else:
            print("Please enter a valid number.")
    while valid_e is False:
        range_end = input("Enter the end of the range: ")
        if range_end.isdigit() and range_first < int(range_end):
            range_end = int(range_end)
            valid_e = True
        else:
            print("Please enter a valid number.")
    num_gen = random.randint(range_first,range_end)
    while valid_v is False:
        guess = input("Guess a number: ")
        if guess.isdigit() and int(guess) == num_gen:
            valid_v = True
        else:
            attempts +=1
    if attempts == 1:
        suffix = ""
    else:
        suffix = "s"

    return f"You guessed the number in {attempts} attempt{suffix}"

