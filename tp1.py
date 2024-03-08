# Types de base
print('I\ Types de base \n')

print(type(True)) #booléen
print(type(10)) #entier
print(type(2.3)) #flottant
print(type('bonjour')) #chaine de caractère

print(5+6)
print(5*3)
print('Bonjour'+'Au revoir')
#Les opérations ne sont possibles que lorsque les objets sont du même type

print(not(False or True)) #Cela renvoie False
print(2==3) #Cela vaut False

print(str(10))
print(str(True))
print(int('20')) #Il est possible de convertir une chaine de caractère en entier que lorsque la chaine de caractère est un nombre

# Instructions de test
print('II\ Instructions de test \n')

def maximum(a,b):
    if a < b:
        return b
    else:
        return a

print(maximum(23,52))

def milieu(a,b,c):
    if a != b != c:
        return b
    else:
        A=maximum(a,b)
        B=maximum(b,c)
        return maximum(A,B)

print(milieu(1,2,3))
print(milieu(1,1,5))

# Les listes
print('III\ Les listes \n')

L=[1,3,'ab',2,'c',0]

print(type(L))
print(len(L))
print(L[3])
# L'indice du premier élèment est 0 et le dernier est len(L) - 1

print([2,3,6]+['ab',8,3])
L.append(3)
print(L)
x=L.pop(L[0])
print(x)
print(L[0:3])

def concatenation(L,M):
    l=[]
    for i in range(0,len(L)):
        l.append(L[i])
    for j in range(0,len(M)):
        l.append(M[j])
    return l

print(concatenation([3,6,5],[23]))

########## fonction sousliste


#La boucle for 
print('IV\ La boucle for \n')

def somme(L):
    s=0
    for i in range(0,len(L)):
        s=s+L[i]
    return s

print(somme([1,2,3]))

# L'appel list(range(10)) devrait retourner une liste des entiers de 0 à 9
# L'appel list(range(2,12)) devrait retourner une liste des entiers de 2 à 11
# L'appel list(range(2,12,3)) devrait retourner une liste des entiers de 2 à 11 avec un pas de 3 c-à-d [2,5,8,11]

print(list(range(10)))
print(list(range(2,12)))
print(list(range(2,12,3)))
print('')
print(list(range(5))) #retourne la liste [0,1,2,3,4]
print(list(range(1,12,2))) #retourne la liste [1,3,5,7,9,11]
print(list(range(13,7,-1)))  #retourne la liste [13,12,11,10,9,8]

# La boucle while
print('V\ La boucle while \n')

def rang(A):
    u=0
    n=0
    while u < A:
        u= u**2 + 3*u + 1
        n=n+1
    return n

print(rang(4))
print(rang(1))



