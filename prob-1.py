a=int(input())
s=input()
q=s.split(',')
#for i in range(a):
    #print(q[i])
cntA=0
cntB=0
change=0
def changes():
    if q[0]=='-':
        if q[1]=='A':
            q[0]=='A'
    if q[a-1]=='-':
        if q[a-2]=='B':
            q[a-1]='B'
    for i in range(1,a-1):
        if q[i+1]=='A' and q[i-1]!='B':
            q[i]=='A'
            change+=1
        elif q[i-1]=='B' and q[i+1]!='A':
            q[i]=='B'
            change+=1
        else:
            continue
changes()
if change!=0:
    change=0
    changes()
else:
    for inp in range(a):
        if q[inp]=='A':
            cntA+=1
        elif q[inp]=='B':
            cntB+=1
if cntA>cntB:
    print('A')
elif cntA==cntB:
    print('Coalition government')
else:
    print('B')

            
