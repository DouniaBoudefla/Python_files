# Produit de matrices

print("Produit d'une matrice\n")

def mat(n,p):
    M=[0]*p
    for i in range(0,p):
        M[i]=[0]*n
    return M

M=mat(4,5)
M[2][3]=3
print(M)

def SommeMat(A,B):
    M=mat(len(A),len(A[1]))
    for i in range(0,len(A)):
        for j in range(0,len(A[1])):
            M[i][j]=A[i][j]+B[i][j]
    return M

print(SommeMat([[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]))

def ProduitMat(A,B): 
    M=mat(len(A),len(B[0]))
    for i in range(0,len(B[0])):
        for j in range(0,len(A)):
            s=0
            for k in range(0,len(A[0])):
                s=s+A[j][k]*B[k][i]
            M[j][i]=s
    return M

print(ProduitMat([[1,2,3],[1,2,3]],[[1,2],[1,2],[1,2]]))

# Opération sur les sous-ensembles finis

print("Opérations sur les sous-ensembles")

def cardinal(R):
    s=0
    for i in range(0,len(R)):
        if R[i]==1:
            s=s+1
    return s

print(cardinal([0,0,1,0,1,1]))

def intersection(R,S): 
    m=0
    if len(R)<len(S):
        m=len(R)
    else:
        m=len(S)
    M=[0]*m
    for i in range(0,m):
        if R[i]==S[i]==1:
            M[i]=1
    ind=0
    for j in range(0,m):
        if M[j]==1:
            ind=j
    for k in range(ind+1,m):
        M.pop()
    return M

print(intersection([0,1,0,1,0,1],[0,1,0,0,1]))

def union(R,S):
    m=0
    if len(R)<len(S):
        m=len(S)
    else:
        m=len(R)
    M=[0]*m
    for i in range(0,len(R)):
        if R[i]==1:
            M[i]=1
    for j in range(0,len(S)):
        if S[j]==1:
            M[j]=1
    return M

print(union([1,0,0,1,1],[0,0,1,1]))

def conv1vers2(R1):
    M=[]
    for i in range(0,len(R1)):
        if R1[i]==1:
            M.append(i)
    return M

print(conv1vers2([0,0,1,0,1,1]))

def conv2vers1(R2):
    a=len(R2)
    M=[0]*(R2[a-1]+1)
    for i in range(0,len(M)):
        for j in range(0,len(R2)):
            if i==R2[j]:
                M[i]=1
    return M

print(conv2vers1([2,4,5]))

def convUnion(R,S): #
    a=conv2vers1(R)
    b=conv2vers1(S)
    c=union(a,b)
    return conv1vers2(c)

def convIntersection(R,S):#
    a=conv2vers1(R)
    b=conv2vers1(S)
    c=intersection(a,b)
    return conv1vers2(c)


print(convUnion([2,4],[5]))
print(convIntersection([2,4,5,6],[1,2,4,5]))
    
# Codes de Gray

print("Codes de Gray\n")

def poids(x):
    s=0
    for i in range(0,len(x)):
        if x[i] == 1:
            s=s+1
    return s

print(poids([1,1,0,0,0,1,0]))

def successeurGray(n,x):
    a=poids(x)
    y=[]
    if a % 2 == 0:
        y=x
        y[n-1]=1-x[n-1]
    bool=True
    M=[0]*(n-1)
    if x[1:n]==M and x[0]==1:
        bool=False
    if a % 2 != 0 and bool==True:
        b=True
        c=0
        for i in range(0,n):
            for j in range(i+1,n):
                if x[i]==1 and x[j] != 0:
                    b=False
                if b==True:
                    c=i
        y=x
        y[c-1]=1-x[c-1]
    if bool==False:
        y=x
    return y

print(successeurGray(4,[1,1,0,0]))
print(successeurGray(6, [1,1,0,1,0,0]))
print(successeurGray(8, [1,0,0,0,0,0,0,0]))

def gray(n):
    G=[]
    x=[0]*n
    G=G+[x]
    y=successeurGray(n, x)
    for i in range(0,(2**n)-1):
        G=G+[y]
        x=y
        y=successeurGray(n, x)
    return G

print(gray(3))

# Suites de Syracuse

print("Suites de Syracuse\n")

def succ(k):
    if k % 2 == 0:
        return k//2
    else:
        return 3*k+1
    
print(succ(16))
print(succ(3))

def syracuse(p,n):
    s0=p
    L=[s0]
    for i in range(1,n):
        s1=succ(s0)
        L.append(s1)
        s0=s1
    return L

print(syracuse(3,10))

def temps(p):
    n=0
    bool=False
    while not(bool):
        L=syracuse(p,n)
        for i in range(0,len(L)):
            if L[i] == 1:
                bool=True
        n=n+1
    return n-2 
# Si la conjecture de Syracuse n'est pas vraie, à l'exécution de cette fonction, le programme pourrait continuer de tourner sans jamais s'arreter

print(temps(3))