
import wordnet_utils

def main():
    wordnetUtils = wordnet_utils.WordnetUtil()
    command = input('w: word transfer, other: end -> ')
    while(command == 'w'):
        target = input("input word: ")
        wordnetUtils.transfer(target)
        command = input('continue: w, escape: other key -> ')

if __name__=="__main__":
    main()