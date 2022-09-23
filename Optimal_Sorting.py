n=int(input())
for i in range(n):
    s=0
    a=int(input())
    b=list(map(int,input().split()))
    if b!=sorted(b):
        print(max(b)-min(b))
    else:
        print('0')