#!/usr/bin/env python3
import math
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

def printPrimeNumberT(startN, value):
	if(startN!=0):
		n = startN + 1
	else:
		n = 0
	value += n
	while n<value:
		n += 1
		try:
			async_result = pool.apply_async(is_prime, (n, ))
			return_val = async_result.get()
			if return_val:
				#print(n)
				pass
		except:
			print ("Errore Thread")
	#print (n)

def printPrimeNumber(startN, value):
	if(startN!=0):
		n = startN + 1
	else:
		n = 0
	value += n
	while n<value:
		n += 1
		if is_prime(n):
			#print(n)
			pass
	#print (n)

def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(n**0.5) + 1, 2))

printPrimeNumber(0, 100)
#printPrimeNumberT(500000000000000, 10000)
#printPrimeNumberT(0, 100)
