# palindromicprimes

This is a Python module to find [palindromic primes](https://en.wikipedia.org/wiki/Palindromic_prime) up to **99999199999**.

## Usage
### Install

``` sh
$ pip install palindromicprimes
```
### How to use
Find the nth palindromic prime:
```python
import palindromicprimes as palprimes

print(palprimes.nthPalindromicPrime(10))
```

Find the lowest nearest palindromic prime to a number:
```python
import palindromicprimes as palprimes

print(palprimes.lowestNearestPalindromicPrime(50000))
```
*Note: this function returns both the index of this prime in the list and the prime itself.*

Created for the NahamCon CTF 2020 (see more [here](https://writeups.noxtal.com/#/posts/2020-06-14-nahamcon-homecooked)).
Based on the A002385 number set.

For more things I did, see my [website](https://www.noxtal.com).