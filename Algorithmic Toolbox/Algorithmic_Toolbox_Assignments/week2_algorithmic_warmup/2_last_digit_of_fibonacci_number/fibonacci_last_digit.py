# Uses python3
import sys

def fibonacci_ld(n):
    fibarray = [0,1]
    for i in range(2,n+1):
        fibarray.append((fibarray[i-2]+fibarray[i-1])%10)
    return fibarray[n]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(fibonacci_ld(n))
