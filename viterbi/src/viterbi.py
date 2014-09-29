'''
Created on 22 Sep 2014
@author: dulshani

Implements the Viterbi Algorithm
words T = 10
states N = 23*
Though Penn Treebank has 45 tags, when trained with the nltk data it gives just 23 tags (Punctuation tags were not considered)
'''
import extract_prob, nltk

sent = "They refuse to permit us to obtain the permit".split()
test = ["START"]
test.extend(sent)

T = 10          #words
N = 23          #states
matrix = []     #matrix of probability multiplications

#Calculate initial state probabilities
trans_prob = []     #transition probabilities
obs_prob = []       #observation probabilities
mult = []

for tag in extract_prob.unique_tags:
    prob = extract_prob.cpd_tags["START"].prob(tag)
    trans_prob.append(prob)

for tag in extract_prob.unique_tags:
    prob = extract_prob.cpd_tagwords[tag].prob(test[1]) 
    obs_prob.append(prob)

mult = [a*b for a,b in zip(trans_prob,obs_prob)]

matrix.append(mult)
    
#Calculate remaining probabilities
for x in range(2, T):
    mult2 = []
    for tag in extract_prob.unique_tags:
        trans_prob = []
        for prev_tag in extract_prob.unique_tags:
            prob = extract_prob.cpd_tags[prev_tag].prob(tag)
            trans_prob.append(prob)
        multx = [a*b for a,b in zip(trans_prob,mult)]
        #Max of probabilities 
        maxm = max(multx)    
        #observation probability of xth word                                
        obs_prob = extract_prob.cpd_tagwords[tag].prob(test[x])
        mul = maxm * obs_prob
        mult2.append(mul)
    mult = mult2
    matrix.append(mult)
    
#Use backoff to get POS
pos_tags = []
tagged_words = []

for column in matrix:
    p = column.index(max(column))
    pos = extract_prob.unique_tags[p]
    pos_tags.append(pos)
    
for word,tag in zip(sent, pos_tags):
    tagged_words.append([word,tag])
    
#POS tags trained to Viberti Algorithm
print tagged_words
#[['They', 'PRO'], ['refuse', 'V'], ['to', 'TO'], ['permit', 'V'], ['us', 'PRO'], ['to', 'TO'], ['obtain', 'V'], ['the', 'DET'], ['permit', 'V']]

#Compare against NLTK output
print nltk.pos_tag(sent)
#[('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('permit', 'NN')]