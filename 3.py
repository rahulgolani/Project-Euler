# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt


# SIMPLE SOLUTION
def getLargestPrime(n):
    result=2
    while n%2==0:
        n=n//2
    for i in range(3,int(sqrt(n))+1,2):
        while n%i==0:
            n=n//i
            result=i
    return result


if __name__ == '__main__':
    n=600851475143
    result=getLargestPrime(n)
    print(result)
