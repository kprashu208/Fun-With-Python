import random

def hangman():

    word = random.choice(["animal", "superman", "avengers", "tiger", "lion", "water",
            "earth", "student", "aeroplane", "railways", "parrot", "pigeon"])

    valid_entries = "abcdefghijklmnopqrstuvwxyz"
    chances = 10
    guess_made = ''

    while len(word) > 0 :

        main_word = ""
        missed = 0

        for letter in word :
            if letter in guess_made :
                main_word = main_word + letter
            else :
                main_word = main_word + "_" + " "

        if main_word == word :
            print(main_word)
            print("Congratulations", name ,",you won the game..!!")
            break

        print("Guess the word:", main_word)
        guess = input()

        if guess in valid_entries :
            guess_made = guess_made + guess
        else :
            print("Invalid input. Please enter a valid guess (lowercase alphabets only)")

        if guess not in word :
            chances -= 1

            if chances == 9 :
                print("9 attempts left !")
                print("   ----------   ")

            if chances == 8 :
                print("8 attempts left !")
                print("   ----------   ")
                print("       0        ")

            if chances == 7 :
                print("7 attempts left !")
                print("   ----------   ")
                print("       0        ")
                print("       |        ")

            if chances == 6 :
                print("6 attempts left !")
                print("   ----------   ")
                print("       0        ")
                print("       |        ")
                print("      /         ")

            if chances == 5 :
                print("5 attempts left !")
                print("   ----------   ")
                print("       0        ")
                print("       |        ")
                print("      / \       ")

            if chances == 4 :
                print("4 attempts left !")
                print("   ----------   ")
                print("     \ 0        ")
                print("       |        ")
                print("      / \       ")

            if chances == 3 :
                print("3 attempts left !")
                print("   ----------   ")
                print("     \ 0 /      ")
                print("       |        ")
                print("      / \       ")

            if chances == 2 :
                print("2 attempts left !")
                print("   ----------   ")
                print("     \ 0 /|     ")
                print("       |        ")
                print("      / \       ")

            if chances == 1 :
                print("1 attempt left !")
                print("Last Attempt amigo...!! ALL THE BEST")
                print("   ----------   ")
                print("     \ 0_|/     ")
                print("       |        ")
                print("      / \       ")

            if chances == 0:
                print("   ----------   ")
                print("       0_|      ")
                print("      /|\       ")
                print("      / \       ")
                print(" You Let A Good Man Die...")
                print(" YOU LOSE :(")
                break



name = input("Enter your name...!!\n")
print("Welcome to the Hangman Game,", name)
print("--------------------------------------")
print("Try to guess the word in less than 10 chances")
hangman()
print()
