def read_lines(filename):
    lines = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            lines.append(line)
    return lines

def preprocess_lines(lines):
    preproc_lines = []
    for line in lines:
        line = line.lower()
        line = line.replace('-', ' ')
        line = line.translate(str.maketrans('', '', string.punctuation))
        preproc_lines.append(line)

    return preproc_lines

def create_dictionary(sentences):
    word_dict = {}    
    for sentence in sentences:
        sentence = sentence.split()
        for word in sentence:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    return word_dict

def get_top_word(word_dict):
    top_word = max(word_dict, key = word_dict.get)
    return top_word

def display_top_words(word_dict):
    COUNT = 10
    print(f'The {COUNT} most frequent words are:')
    for num in range(COUNT):
        top_word = get_top_word(word_dict)
        print(f'\tCount {max(word_dict.values())}: {top_word}')
        del word_dict[top_word]

def main():
    FILENAME = 'text.txt'
    #Getting text and preprocessing
    lines = read_lines(FILENAME)
    sentences = preprocess_lines(lines)
    #Creating dictionary
    word_dict = create_dictionary(sentences)

    display_top_words(word_dict)
    
main()
