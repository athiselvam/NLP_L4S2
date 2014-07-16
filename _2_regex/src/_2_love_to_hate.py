'''
Convert a love song to a hate song!

Created on 15 Jul 2014

@author: dulshani
'''

import re

def love_to_hate(song):
    with open(song) as original: 
        love = original.read()
        original.close()
        print "THIS IS THE LOVE SONG!\n" + love + "\n"
        pattern = 'kiss|miss'
        replacement = 'hit'
        hate = re.sub(pattern, replacement, love)
        print "LETS TURN LOVE TO HATE!\n" +  hate + "\n"
    with open("hate.txt", "w+") as modified:
        modified.write(hate)
        modified.close()
    
def main():
    print "TEST"
    test = "abba.txt"
    love_to_hate(test)    
    fin = raw_input("Enter file name: ")  
    love_to_hate(fin)   

if __name__ == '__main__':
    main()