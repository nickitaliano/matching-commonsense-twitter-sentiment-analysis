#!/usr/bin/env python
'''
  Description : Part of Speech (Identifying the word category)
'''
import nltk
# string = "Life is very beautiful! How?"
# string = "I have been waiting for you since 2010"
string = "Semantic Web is an extension of the current web"
words = nltk.word_tokenize(string)
'''
Tag		Meaning		Examples
ADJ	adjective		new, good, high, special, big, local
ADV	adverb			really, already, still, early, now
CNJ	conjunction		and, or, but, if, while, although
DET	determiner		the, a, some, most, every, no
EX	existential		there, there's
FW	foreign word	dolce, ersatz, esprit, quo, maitre
MOD	modal verb		will, can, would, may, must, should
N	noun			year, home, costs, time, education
NP	proper noun		Alison, Africa, April, Washington
NUM	number			twenty-four, fourth, 1991, 14:24
PRO	pronoun			he, their, her, its, my, I, us
P	preposition		on, of, at, with, by, into, under
TO	the word to		to
UH	interjection	ah, bang, ha, whee, hmpf, oops
V	verb			is, has, get, do, make, see, run
VD	past tense				said, took, told, made, asked
VG	present participle		making, going, playing, working
VN	past participle			given, taken, begun, sung
WH	wh determiner			who, which, when, what, where, how
'''
pos =  nltk.pos_tag(words)
for i in pos:
	print i

