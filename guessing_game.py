import random

print('''
---------------------------------------
The Random Number Guessing Game Begins!
---------------------------------------
''')

scores = []

def start_game():
    global scores
    randomNumber = random.randint(1, 10)
    attempts = 0

    if scores:
        print(f"\n------ The HIGHSCORE is {min(scores)} ------")
    
    while True:
        attempts += 1
            
        try:
            player_guess = input('Guess a number between 1 and 10: ')
            player_guess = int(player_guess) 
            if player_guess < 1 or player_guess > 10:
                print("You must enter a number from 1 to 10.")
                continue
            elif player_guess < randomNumber:
                print("It's higher!")
                continue
            elif player_guess > randomNumber:
                print("It's lower!")
                continue
        except (ValueError, TypeError) as err:
            print("That's not a valid value. Try again.")
            print("({})".format(err))
        else:
            print(f"\nYou got it! It took you {attempts} attempt(s) to guess the number {randomNumber}.")
            scores.append(attempts)
            player_response = input("Would you like to play again? [y]es/[n]o: ")
            
            if player_response.lower() in ('y', 'yes'):
                start_game()
            break

# Kick off the program by calling the start_game function.
start_game()

print('''
----------------------------
Game over. Hope you had fun!
----------------------------
''')