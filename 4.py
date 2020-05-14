# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

'''
def getLargestPalindromic():
    result=0
    #The solution lies between 100 and 999
    for a in range(100,1000):
        for b in range(100,1000):
            #Checking every Number for palindrome
            if isPalindrome(a*b):
                result=max(result,a*b)
    return result
'''

'''
The above solution checks numbers twice. This can be optimized if assuming a<=b
'''

'''
def getLargestPalindromic():
    result=0
    #The solution lies between 100 and 999
    for a in range(100,1000):
        for b in range(a,1000):
            #Checking every Number for palindrome
            if isPalindrome(a*b):
                result=max(result,a*b)
    return result
'''


'''
Further optimization can be to start from 999 and count up to 100. This wasy we can find the result more quickly
'''

'''
def getLargestPalindromic():
    result=0
    #The solution lies between 100 and 999
    for a in range(999,99,-1):
        for b in range(a,99,-1):
            #Checking every Number for palindrome
            if isPalindrome(a*b):
                result=max(result,a*b)
                break
    return result
'''

'''
Let N = 3, then the product will contain atleast 6 digits. Since the product will be a palindrome it will be of the form “abccba” where a, b, c are digits at their respective place value.

“abccba” = 100000a + 10000b + 1000c + 100c + 10b + 1a
= 100001a + 10010b + 1100c
= 11.(9091a + 910b + 100c)

Approach: From the above observation, a pattern can be observed that every palindrome product will always have a factor 11.

For any N digit numbers P and Q, if the product of P and Q is a palindrome, then either P or Q is divisible by 11 but not both of them.
Therefore, instead of checking whether the product of P and Q is a palindrome for all the possible pairs of P and Q, we can reduce the number of computations by checking only for the multiples of 11 for one of the numbers.
'''

def getLargestPalindromic():
    result=0
    a=999
    for i in range(a,99,-1):
        if a % 11 == 0:
            b=999
            db=1
        else:
            b=990
            db=11
        for j in range(b,99,-db):
            if isPalindrome(i*j):
                result=max(result,i*j)
                break
    return result



def isPalindrome(n):
    if n==0:
        return True
    return n==reverse(n,0)

def reverse(n,rev):
    if n==0:
        return rev
    rem=n%10
    rev=10*rev+rem
    return reverse(n//10,rev)

if __name__ == '__main__':
    print(getLargestPalindromic())
