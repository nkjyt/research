import json
from nltk.corpus import wordnet

def getWordsFromJson(path, return_value_is_key = False, is_all_return = False):
    f = open(path)
    f_content = json.load(f)

    if is_all_return:
        return f_content

    if(return_value_is_key):
        return f_content.keys()
    else:
        words = []
        for word_in_page in f_content.values():
            words.extend(word_in_page)
        return words

def get_keys(is_return_with_value = False):
    f = open("./data/duplicate_words.json")
    json_data = json.load(f)
    if is_return_with_value:
        return json_data['data']
    else:
        keys = json_data.keys()
        return keys

def get_synonyms(word):
    sys = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            sys.append(lemma.name())
        """ print('Word and Type : ' + synset[0].name())
        print('Synonym of Travel is: ' + synset[0].lemmas()[0].name())
        print('The meaning of the word : ' + synset[0].definition())
        print('Example of Travel : ' + str(synset[0].examples())) """

keys = get_keys()
new_keys = []
for k in keys:
    sys = get_synonyms(k)
    if sys:
        for s in sys:
            if not s in keys:
                new_keys.append(s)

print(new_keys)