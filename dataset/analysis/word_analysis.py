import csv
import json
from os import write

"""
ファイルを順に参照する

"""

#manga_namelist.csvからタイトル名などのデータを取得
def getTitle():
    csv_data = []
    file_path = r"C:\Users\nkjmy\Documents\dataset\manga_namelist.csv"
    csv_file = open(file_path, "r",  encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file,  delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    #print(header)
    for row in f:
        #[1]はタイトル, [4]はエピソード数
        #print(row)
        csv_data.append(row)
    return csv_data

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

def writeToJson(path, value):
    with open(path, 'w') as f:
        json.dump(value, f)

def iterator():
    csv_data = getTitle()

    word_count = {}
    
    for row in csv_data:
        for ep in range(1,int(row[2])+1):
            source = "C:/Users/nkjmy/Documents/dataset/wordlist/" + row[1] + "/" + row[1] + "_ep" + str(ep) + "_wordlist.json"
            word_in_episode = getWordsFromJson(source)

            #単語の出現回数を調べる処理
            for word in word_in_episode:
                try:
                    word_count[word] += 1
                except KeyError:
                    word_count[word] = 1
    
    #回数の降順でソートし、ファイルに保存
    #word_count_sorted = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
    #output = {word_count_sorted[i][0] : word_count_sorted[i][1] for i in range(0,len(word_count_sorted), 2)}
    #with open('./data/word_count_old.json', 'w') as f:
     #   json.dump(output, f)

    k = word_count.keys()
    return k
    

def check_empty_word():
    manga_keys = iterator()
    json_data = getWordsFromJson("./data/wordfreqlist.json", True, True)
    freq_keys = json_data.keys()
    set_manga = set(manga_keys)
    set_freq = set(freq_keys)
    #重複する単語のset
    dup = set_manga & set_freq

    dup_list = list(dup)
    duplicate_words = {dup_list[i] : json_data[dup_list[i]] for i in range(0,len(dup_list))}
    #writeToJson('./data/duplicate_words.json', duplicate_words)

    not_in_manga = list(set_freq - set_manga)
    not_dup_words = {not_in_manga[i] : json_data[not_in_manga[i]] for i in range(0,len(not_in_manga))}
    
    writeToJson('./data/not_in_manga.json', not_dup_words)
    
    

if __name__=="__main__":
    check_empty_word()