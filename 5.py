# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Simple Solution
from math import sqrt

'''
def getSmallestDivisibleNumber():
    num=40
    while True:
        if isDivisible(num):
            break
        num+=20
    return num

def isDivisible(num):

    for i in range(19,1,-1):
        if num%i!=0:
            return False
    return True
'''

'''
Let N be the smallest number that is divisible by all the integers from 2 to k. For N to be the smallest value with this property we must ensure that in its prime factorisation it does not contain any more prime factors than is absolutely necessary.

Consider the first three cases of k:
k = 2, N = 2
k = 3, N = 2*3 = 6
k = 4, N = 2*3*2 = 12

We can see that for k = 4 we did not need to evaluate 2*3*4, because one of the 2’s in the prime factorisation of 4 = 2*2 was already included. If we now consider the next two cases:

k = 5, N = 2*2*3*5 = 60
k = 6, N = 2*2*3*5 = 60

We can see that N = 60 for both k = 5 and k = 6, because if N contains the factors 2 and 3 it already contains everything necessary for it to be divisible by 6.
Applying this principle for the case k = 20:
N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560
So how do we solve this programmatically?
Let p[i] be the i th prime number: p[1] = 2, p[2] = 3, p[3] = 5, … .
Let N = p[1]^a[1] * p[2]^a[2] * p[3]^a[3] * … ; initially, let a[i] = 0 for all i.
For j = 2 to k, write each j in the form, p[1]^b[1] * p[2]^b[2] * p[3]^b[3] * … and set
a[i] = max(a[i], b[i]).
Let us observe this algorithm with a trace for k = 10.
j b[1] b[2] b[3] b[4] a[1] a[2] a[3] a[4]
2  1                    1
3        1              1    1
4  2                    2    1
5             1         2    1    1
6  1     1              2    1    1
7                  1    2    1    1    1
8  3                    3    1    1    1
9        2              3    2    1    1
10 1          1         3    2    1    1

Hence N = 2^3 * 3^2 * 5^1 * 7^1 = 2520.
However, this approach requires a function to be constructed to express a given number as a product of prime factors. So we shall consider an alternative approach.
'''

def sieveOfEratosthenes(n):
    primeNos=[]
    primes=[True]*(n+1)
    p=2

    while p*p<=n:
        if primes[p]==True:
            for i in range(p*p,n+1,p):
                primes[i]=False
        p+=1

    for i in range(2,len(primes)):
        if primes[i]:
            primeNos.append(i)
    return primeNos

def getFactor(n):
    factor={}
    i=0
    while n%2==0:
        i+=1
        n=n//2
    if i>0:
        factor[2]=i
    for j in range(3,int(sqrt(n))+1,2):
        i=0
        while n%j==0:
            i+=1
            n=n//j
        if i>0:
            factor[j]=i
    if n>=2:
        factor[n]=1
    return factor


def getSmallestDivisibleNumber(n):
    primeNos=sieveOfEratosthenes(n)
    # print(primeNos)
    map={}
    for i in range(len(primeNos)):
        map[primeNos[i]]=0
    # print(map)

    for i in range(2,n+1):
        factor=getFactor(i)
        for j in factor:
            # print(factor)
            map[j]=max(map[j],factor[j])
    # print(map)
    result=1
    for i in map:
        result=result*(i**map[i])

    return result

if __name__ == '__main__':
    print(getSmallestDivisibleNumber(20))
