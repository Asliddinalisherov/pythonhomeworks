a,b,c=map(int,input().split())
max=0
min=0
if a>=b and a>=c:
    max=a
elif b>=a and b>=c:
    max=b
else:
    max=c

if a<=b and a<=c:
    min=a
elif b<=a and b<=c:
    min=b
else:
    min=c

print(max,min)