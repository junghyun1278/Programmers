def gcd(n, m):
    if n >m:
        (n,m) = (m,n)
    while m != 0:
        (n,m) = (m,n%m)
    return n

def solution(n,m):
    return [gcd(n,m),n*m/gcd(n,m)]