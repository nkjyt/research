#2021-11-04 できる限り単語を成形、文章の形で保存するためのコード
import json
import codecs
import pandas as pd
import re
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from wordnet_utils import WordnetUtil
import wordnet_utils
from collections import deque
import csv


Q = deque()
flag = False
utils = WordnetUtil()


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
    replacements = {'\\xe2\\x80\\x94': '-', '\\xe2\\x80\\x98': '','\\xe2\\x80\\x99': '\'', '_': '', 'xc2xbb' : '', 'xc2xcab' : '','\\': ''}
    '|'.join(map(re.escape, replacements.keys()))
    result = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], ori)
    #result = wn.lemmas(ori)
    #print(result)
    if '-' in result and len(Q) == 0:
        print("changing : " + result)
        #語尾が-でつながる単語、改行される単語
        if result[-1] == '-':
            Q.append(result.replace('-',''))
            return ""
        elif result[0] == '-':
            result.replace('-', '')
            print("changed : " + result)
        else:
            return result
    if len(Q) > 0:
        result = Q.popleft() + result
        result = utils.word_transfer(result)
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
    title = 'EJ01'
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

                #print(v)
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
                    if trans != transfer_old(trans):
                        #print(trans + " : old_transfer : " + transfer_old(trans))
                        trans = transfer_old(trans)
                    if not trans == "":
                        word_tb.append(trans)
                lis = [title, episode, p, tb]
                tb += 1
                #lis.extend(word_tb)
                
                lis.append(list_to_str(word_tb))
                #print(li)

                word_epi.append(lis)
    return word_epi

def list_to_str(li):
    result = ""
    if li != []:
        result = li[0]
        if len(li) > 1:
            for i in range(1,len(li)):
                result += "," + li[i]
    return result

#単語リスト作成時にstopwordを省き、荒めに省く
def transfer_old( ori ):#単語の原形に変換したり，明らかに変な認識の単語を省きます
    if(ori!=None):
        trans = wn.morphy(ori)
        trans_ADJ = wn.morphy(ori, wn.ADJ)
        if(trans!=None):
            if(trans_ADJ!=None):
                if(trans==ori):
                    #print('--- '+ ori)
                    #print(trans)
                    return trans
                else:
                   # print(' >>> '+ ori)
                   # print(trans_ADJ)
                    return trans_ADJ
            else:
               # print('>>> '+ ori)
               # print(trans)
                return trans
        else:
        #    print("deleted  :  " + ori)
            return ''
   # print("deleted" + ori)
    return ''

def writeCSV(data):
    with open('word_data_EJ01_ep1_word_only.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


data = loadData()
writeCSV(data)

