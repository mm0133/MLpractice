# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

tr_n = int(sys.stdin.readline())
tr_data = []
for i in range(tr_n):
    tr_data.append(list(map(float, sys.stdin.readline().split())) + [i])
te_n = int(sys.stdin.readline())
te_data = []
for i in range(te_n):
    te_data.append(list(map(float, sys.stdin.readline().split())))


# tr_n  te_n  tr_data te_data

def mean(s):
    if s:
        m = sum(s) / len(s)
    else:
        m = 0
    return m


def var(s):
    if s:
        m = mean(s)
        vsum = 0
        for i in s:
            vsum += (i - m) ** 2
        v = vsum / len(s)
    else:
        v = 0
    return v


def get_r(Ssmall, Slarge):
    ys = list(map(lambda x: tr_data[x][12], Ssmall))
    yl = list(map(lambda x: tr_data[x][12], Slarge))
    r = -var(ys) * len(ys) - var(yl) * len(ys)
    return r


# ys=list(map(lambda x:tr_data[x][12], [0,1,2]))

# print(ys)


class Node:
    def __init__(self, s,h):
        self.S = s[:]
        self.c = None
        self.v = None
        self.right = None
        self.left = None
        self.h=h

height=20

def construct(node):
    global height
    yv = list(map(lambda x: tr_data[x][12], node.S))
    print(yv)
    print(mean(yv))
    if var(yv) and node.h<height:

        maxr = -(1 << 20)
        aSl=[]
        aSs=[]
        for i in node.S:
            for j in range(12):
                xij = tr_data[i][j]
                Ss = []
                Sl = []
                for k in node.S:

                    if tr_data[k][j] > xij:
                        Sl.append(k)
                    else:
                        Ss.append(k)
                if Ss and Sl:
                    curr = get_r(Ss, Sl)
                    if maxr < curr:
                        maxr = curr
                        mini = i
                        minj = j
                        aSl = Sl[:]
                        aSs = Ss[:]
        if aSs and aSl:
            node.c = (mini, minj)
            lnode = Node(aSs,node.h+1)
            rnode = Node(aSl,node.h+1)
            node.l = lnode
            node.r = rnode
            construct(lnode)
            construct(rnode)
        else:
            node.v = mean(yv)


    else:
        node.v = mean(yv)


def find(node, xi):
    if node.v:
        return node.v
    else:
        if tr_data[node.c[0]][node.c[1]] < xi[node.c[1]]:
            return find(node.r, xi)
        else:
            return find(node.l, xi)


root = Node([i for i in range(tr_n)],0)
construct(root)

for xi in te_data:
    print(format(round(find(root, xi), 3),".3f"))

