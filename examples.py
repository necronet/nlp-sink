import argparse
from nltk.corpus import brown, webtext, stopwords
from nltk import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from string import punctuation


def webtext_example():
    #Get raw text for the webtext dictionary
    for fileid in webtext.fileids():
        raw_text = webtext.raw(fileid)
        for i, line in enumerate(raw_text.split('\n')):
            print('[{}] {} : {}'.format(fileid, i,line))


#Tokenizer by default it uses the PUNKT algorithm
def tokenize_example():
    singles = webtext.raw('singles.txt')
    singles_no_8 = singles.split('\n')[8]
    print('[singles] Line:8 - {}'.format(singles_no_8))

    print('\n-----\n'.join(sent_tokenize(singles_no_8)))

    print('Word tokenizer')
    for i,sent in enumerate(sent_tokenize(singles_no_8)):
        print('{}: {}'.format(i,word_tokenize(sent)))

def stopwords_example():
    singles = webtext.raw('singles.txt')
    singles_no_8 = singles.split('\n')[8]
    stopwords_en = stopwords.words('english')
    single_no8_tokenized_lowered = list(map(str.lower, word_tokenize(singles_no_8)))
    stopwords_en = set(stopwords.words('english'))
    stopwords_en_withpunct = stopwords_en.union(set(punctuation))

    print([word for word in single_no8_tokenized_lowered if word not in stopwords_en_withpunct])

def stemming_example():
    porter = PorterStemmer()
    for word in ['walking', 'walks', 'walked','running','raining','rained','runned']:
        print(porter.stem(word))

def lemmatization_example():
    wnl = WordNetLemmatizer()
    for word in ['walking', 'walks', 'walked','running','raining','rained','runned']:
        print(wnl.lemmatize(word))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A Sink of different example of NLTK')
    parser.add_argument('example', metavar='example',
                        help='Select the example you want to run [webtext|tokenize|stopwords|stemming|lemma]')

    args = parser.parse_args()
    if(args.example.lower() == 'webtext'):
        webtext_example()
    elif(args.example.lower() == 'tokenize'):
        tokenize_example()
    elif(args.example.lower() == 'stopwords'):
        stopwords_example()
    elif(args.example.lower() == 'stemming'):
        stemming_example()
    elif(args.example.lower() == 'lemma'):
        lemmatization_example()
    else:
        parser.print_help()
