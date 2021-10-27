from nltk.corpus import wordnet as wn

class WordnetUtil:
    def __init__(self):
        print('wordnet')

    def transfer( self, ori ):
        trans = wn.morphy(ori)
        if(trans!=ori):
            print(ori + '---->' + trans)