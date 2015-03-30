global a, b

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def fibo(index):
	global calls
	calls = 0
	def sub_fib(index):
		global calls
		if index <= 1:
			calls +=1
			return index
		else:
			return sub_fib(index - 1) + sub_fib(index - 2)
	return sub_fib(index), calls           

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

def fibI():
	a, b = 0, 1
	while True:
		a,b = b, a+b
		yield a

def printer(f,r):
	for i in range(r):
		print(next(f))

#print(fibo(100))

fib(354224848179261915075 + 1) #fibonacci fino a 100
#f = fibI()
#printer(f, 100)

#for i in range(100 + 2):
#	print(F(i))