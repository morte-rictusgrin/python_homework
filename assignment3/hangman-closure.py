#Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        result = "".join([letter if letter in guesses else "_" for letter in secret_word])
        print(result)
        return result == secret_word     
    return hangman_closure
secret = input("Enter secret word: ")
game = make_hangman(secret)

while True:
    guess = input("Guess a letter: ")
    is_complete = game(guess)  
    if is_complete:
        print("Congratulations! You won!")
        break

