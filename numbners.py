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
