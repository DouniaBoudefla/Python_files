# Produit d'une suite de matrice 
print("Produit d'une suite de matrices\n")

print(" 1) Dans le premier cas, on a besoin de 12 multiplications d'entiers Et dans le second cas, on a besoin de 6 multiplications d'entiers" )
print("\n")
print("2)")
print("n = 2, A1xA2 1 > 2^2-2 =1")
print("n=3 , A1,A2,A3, A1(A2A3) et (A1A2)A3 2 > 2")
print("n=4 , A1,A2,A3,A4  A((BC)D) A(B(CD)) (AB)(CD) ((AB)C)D (A(BC))D 5 > 4")
print("Initialisation : Ok pour n=2")
print("Hérédité: supposons qu’il y a au moins 2^n-2 parenthésages de A1……An, montrons qu’il y en a > 2^n-1 pour A1……An+1")
print("A partir d’un parenthésage de A1…..An, on peut produire 2 parenthésages de A1…….An+1 :")
print("-On l’applique a A1……An puis on met An+1 à la fin")
print("-On l’applique à A2……An+1 puis n met A1 au début ")
print("Tous ces parenthésages sont distincts donc en tout il y en a >= 2x2^n-2 = 2^n-1")
print("\n")
print("3)")
print("(Ai.....Ak)x(Ak+1......Aj)")
print("On a pour (Ai.....Ak) min=m(i,k) ")
print("On a pour (Ak+1......Aj) min=m(k+1,j)")
print("Et pour x : p(i-1)p(k)p(j)")
print("\n")


def matrixMultCout(p):
    M=[0]*(len(p)-1)
    for k in range(0,len(M)):
        M[k]=[0]*(len(p)-1)
    for d in range(1,len(M)):
        for i in range(0,len(M)-d+1):
            j=i+d-1
            for k in range(i,j):
                acc=M[i][k]
                acc=min(acc,M[k+1][j])
                acc=min(acc,p[i-1]*p[k]*p[j])
                M[i][j]=acc
    return M


def MatrixMultSol(p):
    s=""
    n=len(p)
    M=[0]*(n-1)
    for k in range(0,n-1):
        M[k]=[0]*(n-1)
    for d in range(1,n-1):
        for i in range(0,len(M)-d+1):
            j=i+d-1
            for k in range(i,j):
                acc=M[i][k]
                acc=min(acc,M[k+1][j])
                acc=min(acc,p[i-1]*p[k]*p[j])
                M[i][j]=acc
                s=s+"(A"+str(k)+")"
    print(s)
    return M[1][1]

# Coupe de tige
print("Coupe de tige\n")

print("1)")
print("Rn=max(p1,....,pn; R1+Ri-1,R2+Ri-2,....,Rn-1+R1")

def prixVenteMax(p,n):
    r=[0]*(n+1)
    for i in range(0,n):
        q=0
        for j in range(0,i):
            q=max(p[j],r[i-j])
        r[i]=q
    return r[n]

