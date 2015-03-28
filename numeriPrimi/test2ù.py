#!/usr/bin/env python

def prime(n):
	"""
	Generate all prime numbers less than n.
	"""
	yield 2
	primes = []
	for m in range(3,n,2):
		if all(m%p for p in primes):
			primes.append(m)
			yield m

a = prime(10000)
a=list(a)
print(a)