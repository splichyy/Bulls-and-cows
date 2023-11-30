"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Šplíchal
email: p.splichal98@gmail.com
discord: Petr Š
"""
import random
import time

sep = "-" * 47

def greeting():
    """
    Pozdrav
    """
    print("Hi there!")
    print(sep)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(sep)
    print("Enter a number:")
    print(sep)

def rand_number():
    """
    Generátor náhodného čtyřmístného čísla
    """
    nums = list(range(1, 10))
    random.shuffle(nums)
    while nums[0]== 0:
        random.shuffle(nums)
    return nums[:4]

def guess_rating(secret_number, guess):
    """
    Ohodnotí uživatelem zadané číslo
    """
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    return bulls, cows

def game():
    greeting()
    random_number = rand_number()
    attempts = 0
    start_time = time.time()
    while True:
        guess = input(">>> ")

        if not guess.isdigit() or len(guess) != 4 or guess[0] == '0' or len(set(guess)) < 4:
            print(f"Incorrect guess. Enter correct 4 digit number\n{sep}")
            continue

        attempts += 1
        guess_list = []
        for num in guess:
            guess_list.append(int(num))
         
        bulls, cows = guess_rating(random_number, guess_list)

        if bulls == 4:
            end_time = time.time()
            game_time = round(end_time - start_time, 2)
            print(f"{sep}\nCorrect, you've guessed the right number in {attempts} guesses!")
            print(f"Total game time was {game_time} seconds.")
            break
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}\n{sep}")

if __name__ == "__main__":
    game()