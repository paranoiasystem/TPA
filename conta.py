def conta(string):
	dictionary = {}
	for letter in string:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1
	return dictionary

risultato = conta("marco")
print(risultato)