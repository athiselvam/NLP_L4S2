'''
Created on 9 Jul 2014

@author: dulshani
'''

def find_longest_word(word_list):
    longest_word = '' 
    longest_length = 0
    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word 
    print "Longest word is %s of length %d" %(longest_word, longest_length)


def main():
    test = "Caesar cipher I much prefer Caesar salad"
    test_list = test.split()
    print "TEST"
    find_longest_word(test_list)
    sentence = raw_input("ENTER LIST OF WORDS SEPERATED BY SPACES: ")
    find_longest_word(sentence.split())

    
if __name__ == '__main__':
    main()