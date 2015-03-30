import itertools

def stampa(a):
	while True:
		yield next(a)
		pass

a = itertools.permutations("ABCDEFGHILMNO")

print(list(stampa(a)))
