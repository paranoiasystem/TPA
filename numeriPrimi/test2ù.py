#!/usr/bin/env python

def prime(n):
	yield 2
	primes = {}
	for m in range(3,n,2):
		if all(m%p for p in primes):
			primes.get(m)
			yield m

a = list(prime(1000000))
#a=list(a)
#print(a)