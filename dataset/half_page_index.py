#2021-11-04 Yuta Nakajima
import glob
import codecs
import pandas as pd

#半ページのどちらにあるか
def half_index():
    output = pd.DataFrame()
    #テキストボックスのテキストを取得
    with codecs.open('./wordlist.csv','r','utf-8','ignore') as f:
        textDF = pd.read_csv(f)

    #ファイル名取得
    files = glob.glob("C:/Users/nkjmy/Documents/dataset/TBoutput_default/*")
    for name in files:
        print(name)
        with codecs.open(name,'r','utf-8','ignore') as f:
            df = pd.read_csv(f)
            
            #左にあるページかどうか row[16]
            df['is_right_page'] = 1
            df.loc[df['pointdownx'] < df['image_width'] / 2, ["is_right_page"]] = 0
            #半ページのインデックス付与 row[17]
            df['half_page_id'] = 0
            #テキスト
            df['words'] = ''
            for index, row in df.iterrows():
                df.iat[index, 17] = row[5]*2-1 - row[16]
                tD = textDF[textDF['title'] == row[1]]
                tD = tD[tD['epi'] == row[2]]
                tD = tD[tD['page'] == row[5]]
                tD = tD[tD['tb'] == row[15]]
                #print(tD['words'])
                try:
                    df.iat[index, 18] = tD['words'].values[0]
                except:
                    df.iat[index, 18] = []
            #df.to_csv('./sample.csv')
            output = pd.concat([output, df])
    
    output.to_csv("sample.csv")
            



    


def main():
    half_index()

if __name__=="__main__":
    main()

