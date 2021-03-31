# Uses python3
def fibonacci(n):
    fibarray = [0,1]
    for i in range(2,n+1):
        fibarray.append(fibarray[i-2]+fibarray[i-1])
    return fibarray[n]

n = int(input())
print(fibonacci(n))
