#!/usr/bin/env python3
import re

def wordCounter(stringa):
	return len(re.compile('[a-zA-Z]+').findall(stringa))

#print(len(re.compile('[a-zA-Z]+').findall("Ciao a tutti, come va? Tutto bene")))
print(wordCounter("ciao mondo.affsg. afag faf fafa "))