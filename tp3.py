# Opérations sur les arbres
print("Opérations sur les arbres\n")

def Nombres_Feuilles(T):
        if type(T)==int:
            return 1
        else:
            s=0
            for i in range(0,len(T)):
               s=s+Nombres_Feuilles(T[i])
            return s

print(Nombres_Feuilles([0,[1,2,3]]))

def Somme_étiquette(T):
    s=0
    if type(T)==int:
        s=s+T
    else:
        for i in range(0,len(T)):
            s=s+Somme_étiquette(T[i])
    return s
print(Somme_étiquette([0,[1,2,3,4]]))
print(Somme_étiquette([0,[1,2,[1,2]]]))

def symetrique(T):
    if type(T)==int:
        return T
    else:
        M=[]
        for i in range(len(T)-1,-1,-1):
            x=symetrique(T[i])
            M.append(x)
        return M
    
print(symetrique([[1,2,3],[4,5,6]]))

def Arbre_egaux(A,B):
    S1=symetrique(A)
    S2=symetrique(B)
    if type(A)==type(B) and type(A)== int:
        return S1 == S2
    elif type(A) != type(B):
        return S1 == S2
    else:
        if S2==A or S2==S1 or S1==B:
            return True 
print(Arbre_egaux([0,[1,2,3]],[[3,2,1],0]))

# Courbes définies récurssivement
print("Courbes défnies récurssivement\n")

import matplotlib.pyplot as plt

plt.axis([-0.5,1.5,-0.5,1.5])
for i in range(11):
    plt.plot([0,1],[i*0.1,i*0.1],color="b")
    plt.plot([i*0.1,i*0.1],[0,1],color="b")
plt.show()

def courbe(A,B,n):
    if n==0:
        plt.axis([-2,2,-2,2])
        plt.plot([A[0],B[0]],[A[1],B[1]])
        plt.show()
        











