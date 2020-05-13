'''
SIMPLE SOLUTION
def getSum(n):
    a,b,total=0,1,0
    while b<n:
        c=a+b
        if c%2 == 0:
            total+=c
        a=b
        b=c
    return total
'''

'''
Now let us see if we can get rid of the testing for even values.
Here is the beginning of the Fibonacci sequence with even numbers denoted by c:
1 1 2 3 5 8 13 21 34 55 89 144 ...
a b c a b c  a  b  c  a  b  c
It is easy to prove that every third Fibonacci number is even.
It is not so difficult to change the program somewhat so that only every third number is
added:
'''

'''
def getSum(n):
    a,b,total=1,1,0 #start from 1
    c=a+b
    while c<n:
        total+=c
        a=b+c #computes the next a in sequence
        b=a+c #computes the next b in sequence
        c=a+b #computes the next c in sequence
    return total
'''

'''
There is another beautiful structure hidden beneath this problem:
If we only write the even numbers:
2 8 34 144...
it seems that they obey the following recursive relation: E(n)=4*E(n-1)+E(n-2).
If we can prove that for the Fibonacci numbers the formula F(n)=4*F(n-3)+F(n-6) holds we
have proven this recursion.

F(n) = F(n-1) + F(n-2)
= F(n-2)+F(n-3)+F(n-2)=2 F(n-2) + F(n-3)
= 2(F(n-3)+F(n-4))+F(n-3))=3 F(n-3) + 2 F(n-4)
= 3 F(n-3) + F(n-4) + F(n-5) + F(n-6)
= 4 F(n-3) + F(n-6)
'''

def getSum(n):
    a=2
    b=8
    total=a+b
    c=4*b+a
    while c<n:
        total+=c
        a=b
        b=c
        c=4*b+a
    return total

if __name__ == '__main__':
    n=4000000
    result=getSum(n)
    print(result)
