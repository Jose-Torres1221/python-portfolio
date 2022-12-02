FILENAME = 'jokes.txt'
MODE_READ = 'r'
NUM_JOKES = 250
import random

def select_joke_from_file(choice):
    # select the chosen joke number from file and return it
    html_file = open(FILENAME, MODE_READ)
    for choice in range(1,choice+1):
        joke = html_file.readline()
    html_file.close()
    return joke

def generate_random_choice(): 
    # generate a number within the problem specified range
    choice = random.randint(1,250)
    return choice

def display_joke(joke):
    # make us laugh with your joke :)
    print(joke)

def main():
    print('\n Problem: Tell me a joke \n')
    # call helper functions appropriately
    another = 'Y'
    while another == 'Y':
        print('\nLet me tell you a joke!\n')
        choice = generate_random_choice()
        joke = select_joke_from_file(choice)
        display_joke(joke)
        another = input("Input 'Y' or 'y' if you want to hear another hilarious joke! ")
        another = another.capitalize()
		
main()
