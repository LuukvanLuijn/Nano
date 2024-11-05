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
