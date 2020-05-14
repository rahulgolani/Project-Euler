# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

'''
We do not know what answer to expect so we will try to solve this problem using trial division. However, if a good upper bound for the target prime is known in advance, using a sieve of Eratosthenes is a much more efficient method.

Some useful facts:

1 is not a prime.

All primes except 2 are odd.

All primes greater than 3 can be written in the form 6k+/-1.

Any number n can have only one primefactor greater than n .

The consequence for primality testing of a number n is: if we cannot find a number f less than or equal n that divides n then n is prime: the only primefactor of n is n itself
'''

def sieveOfEratosthenes():
    prime=[True]*999999
    n=999999
    p=2
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n,p):
                prime[i]=False
        p+=1
    primeNos=[]
    for i in range(2,len(prime)):
        if prime[i]:
            primeNos.append(i)
    return primeNos

def getPrime(n):
    primeNos=sieveOfEratosthenes()
    # print(primeNos)
    # print(len(primeNos))
    return primeNos[n-1]

if __name__ == '__main__':
    print(getPrime(10001))
