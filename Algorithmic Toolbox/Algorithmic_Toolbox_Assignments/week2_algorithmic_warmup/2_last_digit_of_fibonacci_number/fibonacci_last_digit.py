# Uses python3
import sys

def get_fibonacci_last_digit(n):
    fibarray = [0,1]
    for i in range(2,n+1):
        fibarray.append(fibarray[i-2]+fibarray[i-1])
    return fibarray[n]%10

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
