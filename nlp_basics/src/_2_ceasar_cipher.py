'''
Ceasar cipher implemented using ROT-13

Created on 8 Jul 2014

@author: dulshani
'''

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}


def rot13(text):
    rot13_text = ""
    for char in text:
        if char in key.keys():
            rot13_text = rot13_text + key[char]
        else:
            rot13_text = rot13_text + char
    print "APPLY ROT-13\t" + rot13_text


def main():
    test = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    print "TEST CASE\t", test
    rot13(test)
    given_text = raw_input("ENTER TEXT\t")
    rot13(given_text)
    


if __name__ == '__main__':
    main()