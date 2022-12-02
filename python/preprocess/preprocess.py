import search_text, string

def read_lines(filename):
    return search_text.read_lines(filename)

def preprocess_lines(lines):
    preproc_lines = []
    for line in lines:
        line = line.lower()
        line = line.replace('-', ' ')
        line = line.translate(str.maketrans('', '', string.punctuation))
        preproc_lines.append(line)

    return preproc_lines

def create_lexicon(preproc_lines):
    lexicon = set()
    for line in preproc_lines:
        line = line.split()
        for word in line:
            lexicon.add(word)

    return lexicon

def filter_tweet_words(tweets, lexicon):
    NUMBER = 'NUM'
    UNKNOWN = 'UNK'

    for tweet_ind, tweet in enumerate(tweets):
        tweet = tweet.split()  #makes tweet a list of words in tweets
        for word_ind, word in enumerate(
                tweet):  #Gives indices while iterating through list
            if word.isdigit():  #checks ele is number
                tweet[word_ind] = NUMBER
            elif word not in lexicon:  #Check if in lexicon, if not then...
                tweet[word_ind] = UNKNOWN

        tweet = ' '.join(tweet)
        tweets[tweet_ind] = tweet

    return tweets

def main():
    CORPUS_FILENAME = 'corpus.txt'
    TWEETS_FILENAME = 'tweets.txt'

    corpus_lines = read_lines(CORPUS_FILENAME)
    tweets = read_lines(TWEETS_FILENAME)

    preproc_corpus_lines = preprocess_lines(corpus_lines)
    preproc_tweets_lines = preprocess_lines(tweets)

    lexicon = create_lexicon(preproc_corpus_lines)

    tweets = filter_tweet_words(preproc_tweets_lines, lexicon)

    print(*tweets, sep='\n\n\n')

main()
