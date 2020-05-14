def getLargestPalindromic():
    result=0
    for a in range(100,1000):
        for b in range(100,1000):
            if isPalindrome(a*b):
                result=max(result,a*b)
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
