# Comparaison expérimentale de l'efficacité des tri fusion et tri à bulles
print("Comparaison expérimentale de l'efficacité\n")


def fusion(A,B):
    n=len(A)
    m=len(B)
    T=[0]*(n+m)
    i=0
    j=0
    for k in range(0,n+m):
        if i > n-1:
            T[k]=B[j]
            j=j+1
        elif j > m-1:
            T[k]=A[i]
            i=i+1
        elif A[i] <= B[j]:
            T[k]=A[i]
            i=i+1
        else:
            T[k]=B[j]
            j=j+1
    
    return T

print(fusion([1,3,4,5,10],[2,7,9]))

import time

def triFusion(L):
    n=len(L)
    if n <=1:
        return L
    i=int(len(L)//2)
    T1=L[0:i]
    T2=L[i+1:n]
    A=triFusion(T1)
    B=triFusion(T2)
    T=fusion(A,B)
    return T

from random import randint

def triBulle(T):
    n=len(T)
    m=0
    for i in range(0,n):
        for j in range(0,n-1):
            if T[j] > T[j+1]:
                m=T[j]
                T[j]=T[j+1]
                T[j+1]=m
    return T

print(triBulle([2,5,4,6,8,1]))


lx=[1000*n for n in range(1,11)]
L1=[]
for i in range(0,10):
    T=[randint(0,100) for i in range(lx[i])]
    avant=time.perf_counter()
    triFusion(T)
    après= time.perf_counter()
    durée = après-avant
    L1.append(durée)
print(L1)
m=L1[0]
for j in range(0,len(L1)):
    m=min(m,L1[j])
print(m)

L2=[]
for i in range(0,10):
    T=[randint(0,100) for i in range(lx[i])]
    avant=time.perf_counter()
    triBulle(T)
    après=time.perf_counter()
    durée=après-avant
    L2.append(durée)
M=L2[0]
for k in range(0,len(L2)):
    M=max(M,L2[k])
print(M)

import matplotlib.pyplot as plt
 
lx=[1000*n for n in range(1,11)]
ly1=[L1[j] for j in range(0,len(L1))]
ly2=[L2[k] for k in range(0,len(L2))]
plt.plot(lx,ly1)
plt.plot(lx,ly2)
plt.show()

# Exponentiation rapide
print("Exponentiation rapide\n")

def expoNombre(a,n):
    if n==1:
        return a
    elif a % 2 == 0:
        return expoNombre(a**2,n/2)
    else:
        return a * expoNombre(a**2,(n-1)/2)
expoNombre(2,3)

def ProduitMat(A,B): 
    M=[0]*len(B[0])
    for i in range(0,len(B[0])):
        M[i]=[0]*len(A)
    for i in range(0,len(B[0])):
        for j in range(0,len(A)):
            s=0
            for k in range(0,len(A[0])):
                s=s+A[j][k]*B[k][i]
            M[j][i]=s
    return M
def expo(a,n,produit,e):
    
