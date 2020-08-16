d=input()
r=d.split()
arr=input()
l=arr.split()
s=0
a=[]
c=0
b=[]
for i in range(r[0]):
    m=r[1]
    n=r[1]+r[2]
    while m!=-1:
        for j in range(r[1]-m):
            s+=l[j]
            a.append(s)
        for k in range(r[1]+r[2]-n):
            c+=l[k]
            b.append(c)
a.sort(reverse=True)
b.sort(reverse=True)
x=a[0]+a[1]
y=b[0]+b[1]
if y>x:
    print("Right "+y-x)
elif x>y:
    print("Wrong "+x-y)
else:
    print("Both are Right")
        
