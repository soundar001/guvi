a=int(input())
l=[]
d=[]
for i in range (0,a):
        b=(input().split())
        l.append(b)

for j in range (0,len(l)):
    for k in range(len(l[j])):
            d.append(int(l[j][k]))
d.sort()
for m in range (0,len(d)):
    print(d[m],end=" ")
