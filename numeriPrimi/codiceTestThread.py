#!/usr/bin/env python3
import math
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

def primeNumber(startN, value):
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

try:
	async_result = pool.apply_async(primeNumber, (0, 500000, ))
	return_val = async_result.get()
	async_result1 = pool.apply_async(primeNumber, (500000, 500000, ))
	return_val1 = async_result1.get()
except:
	print ("Errore Lancio Thread")