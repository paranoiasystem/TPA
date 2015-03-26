#!/usr/bin/env python3
import re

def wordCounter(stringa):
	diz = {}
	listaParole = re.compile('[a-zA-Z]+').findall(stringa)
	#return len(re.compile('[a-zA-Z]+').findall(stringa))
	for parola in listaParole:
		diz[parola] = diz.get(parola, 0) + 1
	return diz	

def wordCounterLezione(stringa):
	parole = stringa.split()
	diz = {}
	for words in parole:
		diz[words] = diz.get(words, 0) + 1
	return diz

asd = wordCounter("Ciao, a tutti. asd ops! asd test test1 test test a abcd a, b, c, d,")
print (asd)