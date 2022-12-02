def generate_random_number():
    # generate and return a random integer in the specified range
    import random
    correct_value = random.randint(1,100)
    return correct_value

def get_input():
    # prompt the user for their number guess and optionally perform input validation 
    valid = False
    while valid == False:
        try:
            user_guess = int(input('Guess a number from 1 to 100: '))
            if user_guess < 1:
                print('Please guess within the range!')
            elif user_guess > 100:
                print('Please guess within the range!')
            else:
                valid = True
        except ValueError:
            print('Please type an INTEGER within the range!')
    
    return user_guess

def is_correct(user_guess, correct_value):
    # If the user’s guess is too high, display “Too high, try again.” 
    # If the user’s guess is too low, display “Too low, try again.” 
    # If the user guesses the number, congratulate the user and return True; otherwise return False
    if user_guess < correct_value:
        print('Too low, try again!')
        return False
    elif user_guess > correct_value:
        print('Too high, try again!')
        return False
    else:
        print('Congratulations you guessed right!')
        return True

        
def main():
    print('\n Problem: Random Number Guessing Game \n')
    # call helper functions appropriately
    play = 'Y'
    while play == 'Y' or play == 'y':
        correct_value = generate_random_number()
        for guesses in range (1,101):
            user_guess = get_input()
            is_correct(user_guess, correct_value)
            if user_guess == correct_value:
                print(f'Congratulations you guessed the right number in {guesses} guesses!\n')
                break
        play = input('If you want to play again type "Y": ')

    
    print("\nThanks for playing, I'll play one on my own\n")
    #Start Artificial Intelligence
    import random
    correct_value = generate_random_number()
    
    #Setting initial parameters
    min = 1
    max = 100

    #Looping AI until correct
    for guesses in range(1,101):
        AI_guess = random.randint(min,max)
        if AI_guess < correct_value:
            print('I was too low!')
            min = AI_guess
        elif AI_guess > correct_value:
            print('I was too high!')
            max = AI_guess
        else:
            print(f'I got it in {guesses} guesses!')
            break
            
main()
