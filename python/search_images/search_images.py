def read_lines(filename):
    lines = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            lines.append(line)
    return lines

def create_dictionary(lines):
    del lines[0]
    image_dict = {}
    
    for line in lines:
        line = line.split(',')
        tag_set = set()
        for ele in line[2:]:
            tag_set.add(ele)
        image_dict[line[1], line[0]] = tag_set
        
    return image_dict

def get_user_query():
    query_tags = set()
    query = input('Enter search query: ')
    query = query.split(sep = ' ')
    for ele in query:
        query_tags.add(ele)
    return query_tags

def display_matches(query_tags, image_dict):
    print('Results:')
    count = 0
    
    # fix!
    for key in image_dict:
        if query_tags <= image_dict[key]:
            count += 1
            print(f'Image {key[0]}: {key[1]}')
    print(f'{count} matches found.\n')

def main():
    print('\nProblem: Image Search using Tags\n')
    FILENAME = 'search_images.csv'
    cont = 'YES'
    
    # fill in
    lines = read_lines(FILENAME)
    image_dict = create_dictionary(lines)
    while cont == 'YES':
        
        query_tags = get_user_query()
        display_matches(query_tags, image_dict)

        
        #Continuing the loop
        cont = input('Do you want to search again? ')
        cont = cont.upper()
        
    print('\nGoodbye!')
   
main()
