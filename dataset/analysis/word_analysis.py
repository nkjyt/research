import csv
import json

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

def getWordsFromJson(path):
    f = open(path)
    f_content = json.load(f)

    words = []
    for word_in_page in f_content.values():
        words.extend(word_in_page)

    return words

def iterator():
    csv_data = getTitle()

    word_count = {}
    
    for row in csv_data:
        for ep in range(1,int(row[2])+1):
            source = "C:/Users/nkjmy/Documents/dataset/wordlist/" + row[1] + "/" + row[1] + "_ep" + str(ep) + "_wordlist.json"
            word_in_episode = getWordsFromJson(source)
            for word in word_in_episode:
                try:
                    word_count[word] += 1
                except KeyError:
                    word_count[word] = 1
    
    print(word_count)

if __name__=="__main__":
    iterator()