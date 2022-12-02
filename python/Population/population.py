FILENAME = 'population.txt'
MODE_READ = 'r'


def read_file():
    # read in population statistics file
    # return population minimum, maximum, and average
    html_file = open(FILENAME, MODE_READ)
    numbers = [float(line) for line in html_file] #Turn into list, call list methods
    #Finding max and min
    minimum = min(numbers)
    maximum = max(numbers)

    #Finding average
    total = sum(numbers)
    total_numbers = len(numbers)
    average = total/total_numbers
    html_file.close()
    #Return everything
    return minimum, maximum, average
    

def display_output(minimum, maximum, average):
    print(f'The minimum population is {minimum:,}')
    print(f'The maximum population is {maximum:,}')
    print(f'The average population is {average:,.0f}.0') #.0 is for uniformity, just to please my eyes

def main():
    print('\n Problem: Population Data \n')
    # call helper functions appropriately
    minimum, maximum, average = read_file()
    display_output(minimum, maximum, average)
    
main()
