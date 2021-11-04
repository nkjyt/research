#2021-11-04 Yuta Nakajima
import glob
import codecs
import pandas as pd

#半ページのどちらにあるか
def half_index():
    #ファイル名取得
    files = glob.glob("C:/Users/nkjmy/Documents/dataset/TBoutput_default/*")
    print(files)

with codecs.open('wordlist.csv','r','utf-8','ignore') as f:
    df = pd.read_csv(f)
