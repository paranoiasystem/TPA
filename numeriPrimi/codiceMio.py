#!/usr/bin/env python3

def printPrimeNumber(startN, value):
	if(startN!=0):
		n = startN + 1
	else:
		n = 0
	value += n
	while n<value:
		n += 1
		if is_prime(n):
			pass

def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(n**0.5) + 1, 2))

printPrimeNumber(0, 1000000)