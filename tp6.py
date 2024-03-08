# Parours de graphe
print("Parcours de graphe\n")
def Connecte(w,s1,s2):
    file=[s1]
    T=[False]*len(w)
    while file != []:
        t=file.pop()
        if T[t] == False:
            T[t]=True
            for i in range(t,len(w)):
                if w[t][i]==1:
                    file.append(i)
    if T[s2] == True:
        return True 
    else:
        return False

def Connecte1(w,s1,s2):
    P=[]
    file=[s1]
    T=[False]*len(w)
    while file != []:
        t=file.pop()
        if T[t] == False:
            T[t]=True
            for i in range(t,len(w)):
                if w[t][i]==1:
                    file.append(i)
                    P.append(i)
    if T[s2] == True:
        return True and P
    else:
        return False and P

# Labyrinthe
print("Labyrinthe\n")

def lectureFichier(monfichier):
    f=open(monfichier,"r+")
    for line in f:
        print(line,type(line),len(line))
    f.close()
    
lectureFichier("minilaby.txt")

def Mat(monfichier):
    M=[]
    f=open(monfichier,"r+")
    for line in f:
        l=line
        M1=[]
        for i in range(0,len(l)-1):
            if l[i] == "X":
                M1.append(0)
            else:
                M1.append(1)
        M=M+[M1]
    return M 
    f.close()
    
print(Mat("minilaby.txt"))