# Polynômes de l'interpolation de Hermite
print("Polynômes de l'interpolation de Hermite")
print("Question 1\n")
import numpy as np

def Lagrange(A,k):
    B=np.delete(A,k)
    P=np.poly1d(np.poly(B))
    L=P/ P(A[k])
    return L

def interpol_Lagrange(A,F):
    n=len(A)
    P= F[0]*Lagrange(A,0)
    for k in range(1,n):
        P=P+F[k]*Lagrange(A,k)
    return np.poly1d(P)

def interpol_Hermite(A,F,Fp):
    n=len(A)
    Q=np.poly1d([0])
    for k in range(0,n):
        Lk=Lagrange(A,k)
        qk=np.polymul(Lk,Lk)
        qderk=np.polyder(qk,1)
        B=A[k]-A
        C=np.delete(B,k) #On enleve le terme qui vaut 0
        D=1/C #Renvoie le vecteur dont les élèments sont les inverses des élèments de C
        s=np.sum(D) #On somme tous les élèments du vecteur D
        qderk=2*s
        Pk=np.poly1d(F[k]) + np.poly1d([1,-A[k]]) * (Fp[k] - qderk*F[k])
        Q=Q + np.polymul(Pk,qk)
    return Q

A=np.array([-1,0,1])
F=np.cos(A)
Fp=-np.sin(A)

P=interpol_Lagrange(A,F)
Q=interpol_Hermite(A,F,Fp)

import matplotlib.pyplot as plt

l=np.linspace(-np.pi,np.pi,100)

plt.clf() #Permet de supprimer les graphiques précédents
plt.plot(l,np.cos(l),'b')
plt.plot(l,P(l),'g')
plt.plot(l,Q(l),'r')
plt.ylim(-2,1)
plt.show()

print("Question 2\n")

def f(x):
    return  1/(1+25*(x**2))

def fder(x):
    return -50*x/((1+25*(x**2))**2)

plt.plot(l,f(l),'r')
plt.show()

for n in [5,10,20]:
    B=-1+(2/n)*np.arange(0,n+1,1)
    P=interpol_Lagrange(B,f(B))
    plt.plot(l,P(l))
plt.ylim(-2,2)
plt.title('Lagrange')
plt.show()

plt.clf()
plt.plot(l,f(l),'r')
for n in [5,10,20]:
    C=-1+(2/n)*np.arange(0,n+1,1)
    Q=interpol_Hermite(C,f(C),fder(C))
    plt.plot(l,Q(l))
plt.ylim(-2,2)
plt.title('Hermite')
plt.show()