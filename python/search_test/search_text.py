def read_lines(filename):
    lines = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            lines.append(line)
    return lines

def find_matches(query, sentences):
    matches = []
    matched_sentences = []
    for ind in sentences:
        if query in ind:
            matched_sentences.append(ind)
            matches.append(sentences.index(ind))
    return matches, matched_sentences

def display_matches(sentences, matches):
    num_of_matches = len(matches)
    print(f'{num_of_matches} matching lines found: \n')
    for pair in zip(matches, sentences):
        print(f'Line {pair[0]}: {pair[1]}\n')
        
def main():
    print('\nProblem: Search Text \n')
    FILENAME = 'text.txt'

    # Fill in!
    #Reading in text file
    lines = read_lines(FILENAME)
    again = 'YES'

    #Beginning Parameters for Matching
    while again == 'YES':
        query = input('\nEnter Search Query: ')
        sentences = lines

        matches, matched_sentences = find_matches(query, sentences)
        sentences = matched_sentences
        display_matches(sentences, matches)

        again = input('Do you want to search again: ')
        again = again.upper()

    print('Goodbye!')

main()
