x,y=map(int,input().split())
tot=(1*x)+(2*y)
if(x==0 and y%2==0):
    print("YES")
elif(x==0 and y%2!=0):
    print("NO")
elif(tot%2==0):
    print("YES")
else:
    print("NO")