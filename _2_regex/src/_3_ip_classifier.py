'''
Given an IP address classify it as Class A,B,C,D or E. 
Also identifies private addresses, zero addresses, loopback and limited broadcast addresses.
Reference: http://compnetworking.about.com/od/workingwithipaddresses/l/aa042400b.htm

IP CLASS TABLE
A    0.0.0.0      127.255.255.255
B    128.0.0.0    191.255.255.255
C    192.0.0.0    223.255.255.255
D    224.0.0.0    239.255.255.255
E    240.0.0.0    255.255.255.255

PRIVATE IP ADDRESS RANGES
A    10.0.0.0      10.255.255.255
B    172.16.0.0    172.31.255.255
C    192.168.0.0   192.168.255.255

LOOPBACK RANGE
127.0.0.0    127.255.255.255

ZERO ADDRESS RANGE
0.0.0.0    0.255.255.255

LIMITED BROADCAST RANGE
255.0.0.0    255.255.255.255

Created on 14 Jul 2014

@author: dulshani
'''

import re

#validate and then classify
def test(addr):
    v = validate(addr)
    if v == None:
        print "IP address %s is invalid" %addr
    else:
        classify(addr)

#Check if given sequence is an IP address
def validate(addr):
    pattern_ip = '^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    m = re.search(pattern_ip, addr)
    return m
    
#Find class of given IP address
def classify(addr):
    #define patterns for each IP address class
    pattern_a = '^(([01]?[01]?[0-9]|12[0-7])\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'  
    pattern_b = '^((12[89]|1[3-8][0-9]|19[01])\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    pattern_c = '^((19[2-9]|2[01][0-9]|22[0-3])\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    pattern_d = '^((22[4-9]|23[0-9])\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    pattern_e = '^((24[0-9]|25[0-5])\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    
    #store class patterns in dictionary
    ip_dic = {'A':pattern_a, 'B':pattern_b, 'C':pattern_c, 'D':pattern_d, 'E':pattern_e}
    
    #define patterns for private IP addresses
    private = '^(((10\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.))|((172\.)((1[6-9]|2[0-9]|3[0-1])\.))|(192\.168\.))(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.)([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    #define pattern for loopback address
    loopback = '^(127\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'  
    #define pattern for zero address
    zero = '^(0\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'  
    #define pattern for  address
    limited_broadcast = '^(255\.)(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){2}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
    
    #store special address patterns in dictionary
    special_dic = {'private':private, 'loopback':loopback, 'zero':zero, 'limited broadcast':limited_broadcast}
    
    #check for class
    for ip_class, ip_pattern in ip_dic.items():
        m = re.search(ip_pattern, addr)
        if m:
            print "IP address %s belongs to class %s" %(addr, ip_class)
            #catches any zero, private, loopback and limited broadcast addresses
            for special, pattern in special_dic.items():
                if re.search(pattern, addr):
                    print "This is a %s address" %special     
            break


def main():
    print "TEST"
    addresses = ["433.554.22.33", "0.0.1.3", "10.122.0.7", "122.15.25.5", "127.0.255.0", "128.0.0.0", "192.168.0.0", "255.0.255.0", "239.255.255.255"]
    for address in addresses:
        test(address)
    user_address = raw_input("Give IP address: ")
    test(user_address)
    
if __name__ == '__main__':
    main()
