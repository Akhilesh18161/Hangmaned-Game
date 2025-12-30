import random
from wordlist import words
from hangman_ascii import hangman_art


def show_man(wrong_guesses):
    print(hangman_art[wrong_guesses])
    
def show_hint(hints):
    print(" ".join(hints))

def show_answer(answer):
    answer = answer.capitalize()
    print(f"The answer was '{answer}'")
    

def playgame():
    answer = random.choice(words).lower()
    hints = ["_"] * len(answer)
    guessed_letters = set()
    wrong_guesses = 0
    while wrong_guesses != len(hangman_art)-1:
        show_man(wrong_guesses)
        show_hint(hints)        
        
        if "_" not in hints:
            print("You Won!")
            return
        
        guess = input("\nEnter a Letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue
            
        if guess in guessed_letters:
            print(f"You have already guessed {guess}")
            continue
            
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                   hints[i] = guess
        else:
            wrong_guesses += 1
            show_man(6)
    print("\nYou Lose!")
    show_answer(answer)
    return
        
def main():
    while True:
        playgame()
        if input("Do you want to play again? (Y/n): ").upper() != "Y":
           print("Thank You for playing!")
           break
        
        
    
if __name__ == '__main__':
    main()