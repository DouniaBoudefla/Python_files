# Question 1
print("Question 1\n")
import numpy as np

A=np.poly1d([5,4,3,2,1,0])
print(A)

b=np.poly([1,2,3,4,5]) # On crée le vecteur qui contient les coefficients du polynôme dont les racines sont 1,2,3,4,5
B=np.poly1d(b) #Puis on crée le polynomé de degré 5 dont les racines son les entiers 1,2,3,4,5
print(B)

C=np.poly1d([1,0]) # O crée le monôme de degré 1
print(C*B)

# Question 2
print("Question 2\n")

def lagrange(A,k):
    L=1
    X=np.poly1d([1,0])  # On crée le monôme de degré 1
    for i in range(0,k):
        for j in range(0,k):
            if j != i:
                L=L*(X-A[j])/(A[i]-A[j]) # On calcule le polynôme de Lagrange 
    return L

for i in range(0,3):
    P=lagrange([0,1,2],i) # On calcule les différents polynômes de Lagrange au k-ième degré avec k=0,1,2
    print(P)
    
# Question 3
print("Question 3\n")

def interpolation(A,F):
    X=np.poly1d([1,0])
    L=1
    P=0
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if j != i:
                L=L*(X-A[j])/(A[i]-A[j])
        P=P+(L*F[i]) # On calcule le polynôme de Lagrange grâce à la formule donnée et on ajoute la somme des valeurs des points d'interpolations par f donnée par le vecteur F
    return P

print(interpolation([0,1,2],[np.cos(0),np.cos(1),np.cos(2)]))

import matplotlib.pyplot as plt

x=[0,1,2]
y=np.cos(x)
plt.plot(x,y,"r")
plt.show()

# Question 4
print("Question 4\n")

def f(x):
    return 1/(1+25*x**2)

def vecteurA(n):
    A=[]
    for x in np.arange(0,n+1):
        A.append(-1+(2*x)/n)
    return A
print(vecteurA(3))

def vecteurF(n):
    F=[0]*(n+1)
    A=vecteurA(n)
    for i in np.arange(0,n+1):
        F[i]=f(A[i])
    return F
print(vecteurF(3))

#### Tracage des courbes de f et des polynômes interpolateurs de Lagrange de degré 5,10,20
x=np.linspace(-0.9,0.9)  
y1=f(x)
A=vecteurA(5) ; B=vecteurA(10) ; C=vecteurA(20)
F=vecteurF(5) ; G=vecteurF(10) ; H=vecteurF(20)
L1=interpolation(A, F) ; L2=interpolation(B,G) ; L3=interpolation(C,H) 
y2=np.polyval(L1,x) ; y3=np.polyval(L2,x) ; y4=np.polyval(L3,x)
p1=plt.plot(x,y1,"r",label="f(x)")
p2=plt.plot(x,y2,"b",label="Polynôme de Lagrange de degré 5")
plt.legend()
plt.show()
p3=plt.plot(x,y3,label="Polynôme de Lagrange de degré 10")
p4=plt.plot(x,y4,"y",label="Polynôme de Lagrange de degré 20")
plt.legend()
plt.show()
 ## On remarque que le polynôme interpolateur de Lagrange de degré 10 est constant, celui de degré 5 le devient aussi à un moment donné et celui de degré 20 l'est dans un certain intervalle 
 