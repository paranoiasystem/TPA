#!/usr/bin/env python
import sys

def prime(n):
	yield 2
	primes = {}
	for m in range(3,n,2):
		if all(m%p for p in primes):
			primes.get(m)
			yield m

def printPrimeNumber(a):
	while True:
		yield next(a)

def main(argv):
	a = prime(int(argv))
	print(list(printPrimeNumber(a)))

if __name__ == "__main__":
   main(sys.argv[1])