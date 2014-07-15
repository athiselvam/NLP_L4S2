'''
User-defined function to find larger of two numbers

Created on 8 Jul 2014

@author: dulshani
'''

def fmax(a,b):
    if a>b:
        return a
    else:
        return b


def main():
    print "TEST: Max Function"
    num1 = int(raw_input("Enter first number: "))
    num2 = int(raw_input("Enter second number: "))
    max_num = fmax(num1,num2)
    print "Larger number is", max_num

        
if __name__ == '__main__':
    main()