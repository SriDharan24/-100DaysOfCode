def sock_merchant(n,ar):
    pairs=0
    set_ar=set(ar)
    for i in set_ar:
        count=ar.count(i)
        pairs+=count//2
    return pairs
n=int(input())
ar=list(map(int,input().split()))
print(sock_merchant(n,ar))