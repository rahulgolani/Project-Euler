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
