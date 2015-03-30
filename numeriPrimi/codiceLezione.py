def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def listaPrimi(number):
    while True:
        if isPrime(number):
            yield number
        number+=1


res=listaPrimi(range(1000))
print(res)