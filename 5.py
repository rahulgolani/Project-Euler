# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Simple Solution
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

if __name__ == '__main__':
    print(getSmallestDivisibleNumber())
