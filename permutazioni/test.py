# ==================================================
# Calcola le possibili permutazioni di un insieme L.
# ==================================================
# Consideriamo di avere un insieme L = [A,B,C].  L'idea sta nel fatto di far scorrere ogni elemento X, 
# uno alla volta, per tutte le permutazioni di L escludendo l'elemento X. Proviamo ad applicare questa
# idea ad L:
#
# Scelgo A e quindi calcolo le permutazioni di [B C] che sono [B C] e [C B].
# Faccio scorrere A su queste permutazioni e quindi ottengo:
# A B C
# B A C
# B C A
# A C B
# C A B
# C B A
#
# ==================================================
def permutazioni(l):
	if len(l) <= 1: 							# Caso base :)
		yield l									# Ritorniamo l. ATTENZIONE: è un vettore!
	else:
		for i in range(len(l)):					# Per i che va da 0 alla lunghezza di l
			for p in permutazioni(l[1:]):		# Prendo tutte le permutazioni di l escludendo il primo elemento
				yield p[:i] + l[0:1] + p[i:]	# Adesso vado a prendere la permutazione p che mi è stata ritornata e gli inserisco l'elemento i° di l alla i° posizione
			# fine for di p
		# fine for di i
	#fine if
#fine def

# -----------------------------------------------
l = "ABCDEFGHILMNO"#input("Inserisci la stringa da permutare (Ad esempio, ABC) -> ")
for x in permutazioni(l): 
	print(x)
# -----------------------------------------------
