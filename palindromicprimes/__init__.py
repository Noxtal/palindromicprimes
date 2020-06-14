from palindromicprimes.PalindromicPrimes import PALINDROMIC_PRIMES
from functools import lru_cache

def nthPalindromicPrime(n):
    return PALINDROMIC_PRIMES[n]

@lru_cache(maxsize=len(PALINDROMIC_PRIMES))
def lowestNearestPalindromicPrime(a):
    b = -1
    bi = 0
    for i, p in enumerate(PALINDROMIC_PRIMES):
        if p > a: break
        if p <= a and p > b:
            b = p
            bi = i     
    return bi, b