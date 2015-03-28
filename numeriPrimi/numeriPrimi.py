#!/usr/bin/env python3
import math

def printPrimeNumber(stop):
	n = 16000000000000000000
	stop += n
	while n<stop:
		n += 1
		if isPrime(n):
			print(n)


def isPrime(n):
	for x in range(2,n):
		if n % x == 0:
			return False
	return True

printPrimeNumber(1000)