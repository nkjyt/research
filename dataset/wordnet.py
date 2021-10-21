import json
import codecs
import pandas as pd
import re
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from collections import deque
import csv

Q = deque()
flag = False

#-で単語を結合させる
def lemmatizer(word):
    li = []
    lemmatizer = WordNetLemmatizer()
    li.append(lemmatizer.lemmatize(word, pos='a'))
    li.append(lemmatizer.lemmatize(word, pos='r'))
    li.append(lemmatizer.lemmatize(word, pos='n'))
    li.append(lemmatizer.lemmatize(word, pos='v'))
    return li[0]



def transfer(ori):
    replacements = {'\\xe2\\x80\\x94': '-', '\\xe2\\x80\\x99': '\'', '_': '', '\\': ''}
    '|'.join(map(re.escape, replacements.keys()))
    result = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], ori)
    #result = wn.lemmas(ori)
    #print(result)
    if '-' in result and len(Q) == 0:
        if result[-1] == '-':
            Q.append(result.replace('-',''))
            return ""
        else:
            return result
    if len(Q) > 0:
        result = Q.popleft() + result
        lemmatizer(result)
        return result
    
    return result

#タイトルのエピソード数と
def loadLengthData(title, episode):
    with codecs.open('page.csv', 'r', 'utf-8', 'ignore') as f:
        df = pd.read_csv(f)
        df = df[df['title'] == title]
        episodelen = len(df.index)
        df = df[df['epi'] == episode]
        pagelen = df['page'][0]
        return episodelen, pagelen

def loadData():
    title = 'EJ09'
    episode = 1

    epi_max, p_max = loadLengthData(title, episode)
    print(epi_max, p_max)

    df = None
    with codecs.open('wordlist.csv','r','utf-8','ignore') as f:
        df = pd.read_csv(f)

    dft = df[df['title'] == title]
    dfe = dft[dft['epi'] == episode]

    word_epi = []

    for p in range(1, p_max+1):
        word_page = []
        dfp = dfe[dfe['page'] == p]
        #DataFrameのデータ数を取得できる
        #print((len(dfp.index)))

        tb = 0
        for tb in dfp['tb']:
            dftb = dfp[dfp['tb'] == tb]
            for v in dftb['words']:

                print(v)
                v = v.lower()
                v = v.split(',')
                word_tb = []
                for w in v:
                    #[], 改行などを削除
                    w = re.sub('\s|\[|\]|^([a-z].\'[a-z]+)' ,'', w)
                    w = w.strip('\'')
                    w = w.strip('\"')
                    #print(w)
                    #print(transfer(w))
                    trans = transfer(w)
                    if not trans == "":
                        word_tb.append(trans)
                li = [title, episode, p, tb]
                tb += 1
                li.extend(word_tb)
                #print(li)
                word_epi.append(li)
    return word_epi

def writeCSV(data):
    with open('word_data_EJ09_ep1.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


data = loadData()
writeCSV(data)

