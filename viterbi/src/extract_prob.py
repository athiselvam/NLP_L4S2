'''
Created on 22 Sep 2014
@author: dulshani
Estimates probabilities required to implement the viberti algorithm
'''

import nltk, string
from nltk.corpus import treebank

tag_words = []

#Gets (tag,word) pairs from the Treebank corpus
for sent in treebank.tagged_sents(simplify_tags=True):  # @UndefinedVariable
    tag_words.append(("START", "START"))
    tag_words.extend([(tag,word) for (word,tag) in sent])
    tag_words.append(("END", "END"))

#Computing observation probabilities P(w(i)|t(i))
#If in state t, probability of getting word w
cfd_tagwords = nltk.ConditionalFreqDist(tag_words)
cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist) 

#Computing state transition probabilities P(t(i)|t(i-1))
#If in state t(i-1) probability of getting to state t(i)
tags = [tag for (tag,word) in tag_words]
cfd_tags = nltk.ConditionalFreqDist(nltk.bigrams(tags))
cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist) 

#Get list of unique tags
unique_tags_with_punctuations = list(set(tags))
#['', 'FW', 'DET', 'WH', "''", 'VD', '#', '$', ')', 'ADJ', 'PRO', ',', '.', 'TO', 'NUM', 'NP', ':', 'ADV', '``', 'END', 'VG', 'L', 'VN', 'N', 'P', 'S', 'EX', 'V', 'CNJ', 'START', 'UH', '(', 'MOD']
#To improve speed, remove punctuations
translated = [s.translate(None, string.punctuation) for s in unique_tags_with_punctuations]
#['', 'FW', 'DET', 'WH', '', 'VD', '', '', '', 'ADJ', 'PRO', '', '', 'TO', 'NUM', 'NP', '', 'ADV', '', 'END', 'VG', 'L', 'VN', 'N', 'P', 'S', 'EX', 'V', 'CNJ', 'START', 'UH', '', 'MOD']
#remove empty strings
unique_tags = [s for s in translated if s] 
#['FW', 'DET', 'WH', 'VD', 'ADJ', 'PRO', 'TO', 'NUM', 'NP', 'ADV', 'END', 'VG', 'L', 'VN', 'N', 'P', 'S', 'EX', 'V', 'CNJ', 'START', 'UH', 'MOD']
#Get number of tags available after training
#print len(unique_tags)
#23