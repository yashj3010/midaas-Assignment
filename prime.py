import time

######## NATIVE ALGORITHM ###########

def generatePrimes(start,end):
    primes = []
    for i in range(start, end+1): 
        if i>1: 
            for j in range(2,i): 
                if(i % j==0): 
                    break
            else: 
                primes.append(i)
    return primes

######## SieveOfEratosthenes ALGORITHM ###########

def SieveOfEratosthenes(start,end):
    primes = []
    prime = [True for i in range(end+1)]
    p = 2

    while (p * p <= end):
        if (prime[p] == True):
            for i in range(p * p, end+1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, end+1):
        if prime[p]:
            primes.append(p)

    for i in range(len(primes)):
        if primes[i] > start:
            primes=primes[i:]
            break
    return primes

######## TAKE THE INPUT, SELECT ALGO ACCORDING TO IT, RETURN OUTPUT ###########

def giveOutput(algo,LowerLimit,upperLimit):
    primes = []

    ticGenPrimes  = time.perf_counter()

    if(algo == 1):
        primes = generatePrimes(LowerLimit, upperLimit)
    else:
        primes = SieveOfEratosthenes(LowerLimit, upperLimit)

    tocGenPrimes  = time.perf_counter()
    executionTime = tocGenPrimes - ticGenPrimes

    print(primes)
    
    return primes,executionTime
