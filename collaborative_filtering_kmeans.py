import heapq

uN=5
rN=10
M=15
p=[[0]*(rN+1) for i in range(uN+1)]
C=2
for i in range(M):
    il= input().split()
    il[0]=int(il[0])
    il[1]=int(il[1])
    il[2]=float(il[2])
    p[il[0]][il[1]]=il[2]

def cos(x,y):
    xs=0
    ys=0
    dotv=0
    for i in range(len(x)):
        xs+=x[i]**2
        ys+=y[i]**2
        dotv+=x[i]*y[i]
    if dotv == 0:
        return 0
    return dotv/(xs**0.5)/(ys**0.5)

ravg=[0]*(uN+1)
cnt=0
for i in range(1,uN+1):
    cnt = 0
    for j in range(1,rN+1):
        if p[i][j]:
            ravg[i]+=p[i][j]
            cnt+=1
    if cnt:
        ravg[i]/=cnt

Up=[]
for i in range(1,uN+1):
    if i!=C:
        if len(Up)<2:
            heapq.heappush(Up,(cos(p[i],p[C]),i))
        elif cos(p[i],p[C])>Up[0][0]:
            heapq.heappushpop(Up,(cos(p[i],p[C]),i))

k=0
print(Up)
for i in Up:
    k+=i[0]
k=1/k


rui=[0]*(rN+1)
for j in range(1,rN+1):
    tem=0
    for i in range(2):
        if p[Up[i][1]][j]:
            tem+=Up[i][0]*(p[Up[i][1]][j]-ravg[Up[i][1]])
    if tem:
        rui[j] = ravg[C] + k * tem

print(rui)
print(ravg)


