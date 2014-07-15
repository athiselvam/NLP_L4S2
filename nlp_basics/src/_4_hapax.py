'''
Created on 9 Jul 2014

@author: dulshani
'''

def hapax(file_name):
    word_dic={}
    hapax = []
    with open(file_name) as f:
        for line in f:
            words = line.split()
            for word_raw in words:
                word = word_raw.lower().strip()
                if word in word_dic.keys():
                    word_dic[word] += 1
                else:
                    word_dic[word] = 1
    print "Hapax in %s: " %file_name
    for word,count in word_dic.items():
        if count == 1:
            print word,
    print ""

        
def main():
    print "TEST"
    hapax("small_text.txt")
    input_file = raw_input("ENTER FILE NAME: ")
    hapax(input_file)
    
    
if __name__ == '__main__':
    main()