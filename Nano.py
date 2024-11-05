import time, random, sys, subprocess, os
from colorama import Fore, Back, Style

def clear():
    os.system('cls')


def numbers():
    difficulty = input("What difficulty do you want to play? Choose: easy, medium, hard, impossible: ")
    attempts = 5

    if difficulty == "easy":
        print("Guess the number between 1 and 10")
        number = random.randint(1, 11)
    elif difficulty == "medium":
        print("Guess the number between 1 and 20")
        number = random.randint(1, 21)
    elif difficulty == "hard":
        print("Guess the number between 1 and 50")
        number = random.randint(1, 51)
    elif difficulty == "impossible":
        print("Guess the number between 1 and 200")
        number = random.randint(1, 201)
    elif difficulty == "no":
        print("Guess the number between 1 and 10000")
        number = random.randint(1, 10001)
    else:
        print("That is not a valid difficulty.")
        numbers()
        return

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        chosennumber = int(input("What is your guess?: "))

        if chosennumber == number:
            print("Correct! You've guessed the number!")
            break
        elif chosennumber < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts -= 1

    if attempts == 0:
        print(f"\nGAME OVER! The correct number was: {number}")
    else:
        print("YOU WON!")
    nanoXL()
    return

def hangman():
    import random

    words_list = open("words.txt").read().splitlines()
    def hangman():
        word = random.choice(words_list)
        guessed_word = "_" * len(word) 
        attempts = 0  
        max_attempts = 6  
        guessed_letters = [] 

        print("Welcome to Hangman!")
        
        while attempts < max_attempts and "_" in guessed_word:
            print("\nWord to guess: " + " ",(guessed_word))
            print(f"Incorrect attempts: {attempts}/{max_attempts}")
            print("Guessed letters: " + " ",(guessed_letters))

            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try again.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                new_guessed_word = ""
                for index in range(len(word)):
                    if word[index] == guess:
                        new_guessed_word += guess  
                    else:
                        new_guessed_word += guessed_word[index]  
                guessed_word = new_guessed_word
            else:
                attempts += 1  

            hangman_diagram(attempts)

        if "_" not in guessed_word:
            print(f"\nCongratulations! You guessed the word: {word}")
        else:
            print(f"\nGame Over! The correct word was: {word}")
    def hangman_diagram(attempts_left):
        hangman_states = [
            """
            ------
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            ------
            |   |
            O   |
                |
                |
                |
            --------
            """,
            """
            ------
            |   |
            O   |
            |   |
                |
                |
            --------
            """,
            """
            ------
            |    |
            O    |
           /|    |
                 |
                 |
            --------
            """,
            """
            ------
            |    |
            O    |
           /|\\   |
                 |
                 |
            --------
            """,
            """
            ------
            |    |
            O    |
           /|\\   |
           /     |
                 |
            --------
            """,
            """
            ------
            |    |
            O    |
           /|\\   |
           / \\   |
                 |
            --------
            """,
        ]
        print(hangman_states[attempts_left])
    hangman()
    nanoXL()
    return

def nanoXL():
    
    print(Fore.BLUE + "███╗   ██╗ █████╗ ███╗   ██╗ ██████╗     ███████╗████████╗ ██████╗ ██████╗ ███████╗")
    time.sleep(0.08)
    print(Fore.BLUE + "████╗  ██║██╔══██╗████╗  ██║██╔═══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝")
    time.sleep(0.08)
    print(Fore.BLUE + "██╔██╗ ██║███████║██╔██╗ ██║██║   ██║    ███████╗   ██║   ██║   ██║██████╔╝█████╗ ") 
    time.sleep(0.08)
    print(Fore.BLUE + "██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║    ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝ ") 
    time.sleep(0.08)
    print(Fore.BLUE + "██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝    ███████║   ██║   ╚██████╔╝██║  ██║███████╗")
    time.sleep(0.08)
    print(Fore.BLUE + "╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝")

    print("type 1 for numbers\ntype 2 for hangman\ntype 3 to exit")
    game = input("your choice: ")
    clear()
    print("____________________________________________________________________________________________________________________________________________")
    if game == "1":
        numbers()
    elif game == "2":
        hangman()
    elif game == "3":
        exit()
    return
nanoXL()
close = input(Fore.GREEN + "Press enter to exit")
    
