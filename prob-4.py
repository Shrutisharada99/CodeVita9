i=int(input())
d=input()
l=d.split()
s=[]
c=0
cnt=0
r=0
for j in range(i):
  if l[i]==1:
    s[i]='one'
    cnt=2
  elif l[i]==2:
    s[i]='two'
    cnt=1
  elif l[i]==3:
    s[i]='three'
    cnt=2
  elif l[i]==4:
    s[i]='four'
    cnt=2
  elif l[i]==5:
    s[i]='five'
    cnt=2
  elif l[i]==6:
    s[i]='six'
    cnt=1
  elif l[i]==7:
    s[i]='seven'
    cnt=2
  elif l[i]==8:
    s[i]='eight'
    cnt=2
  elif l[i]==9:
    s[i]='nine'
    cnt=2
  elif l[i]==10:
    s[i]='ten'
    cnt=1
    c+=cnt
i.sort()
for k in range(i):
  if l[k]+l[k+1]==c:
      r+=1
if r==1:
    print('one')
elif r==2:
    print('two')
elif r==3:
    print('three')
elif r==4:
    print('four')
elif r==5:
    print('five')
elif r==6:
    print('six')
elif r==7:
    print('seven')
elif r==8:
    print('eight')
elif r==9:
    print('nine')
elif r==10:
    print('ten')


    
