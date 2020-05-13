def getSum(n):
    a,b,total=0,1,0
    while b<n:
        c=a+b
        if c%2 == 0:
            total+=c
        a=b
        b=c
    return total


if __name__ == '__main__':
    n=4000000
    result=getSum(n)
    print(result)
