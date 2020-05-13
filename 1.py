# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

'''
def getSum(n):
    if n<=2:
        return 0
    total=0
    for i in range(n):
        if i%3==0 or i%5==0:
            total+=i
    return total

if __name__ == '__main__':
    n=1000
    result=getSum(n)
    print(result)

'''

# If the problem was to do the same with n as 10000000, this soultion might not be efficient as it can take some time. There is also a probability that the sum variable might overflow

'''
Let’s look at the details of our function and take as example n=3.
We would have to add:
3+6+9+12+......+999=3*(1+2+3+4+...+333)
For n=5 we would get:
5+10+15+...+995=5*(1+2+....+199)
Now note that 199=995/5 but also 999/5 rounded down to the nearest integer.
If we now also note that 1+2+3+...+p=½*p*(p+1) our program becomes:
'''

def getSumUtil(target,i):
    n=target//i
    result=i*((n)*(n+1))//2
    return result

def getSum(n):
    target=n-1
    result=getSumUtil(target,3)+getSumUtil(target,5)-getSumUtil(target,15)
    return result

if __name__ == '__main__':
    n=1000
    result=getSum(n)
    print(result)
