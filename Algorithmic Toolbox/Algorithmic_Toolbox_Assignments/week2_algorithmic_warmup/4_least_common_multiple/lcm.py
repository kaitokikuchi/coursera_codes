# Uses python3
import sys

def euclidGCD(a,b):
  if b == 0:
    return a
  else:
    c = a%b
    return euclidGCD(b,c)

def lcm(a, b):
    gcd = euclidGCD(a, b)
    lcm = a*b/gcd
    return int(lcm)

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))

