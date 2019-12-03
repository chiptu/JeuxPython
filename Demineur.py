import random 
def afficher(M):
# affiche la matrice
    for i in range(len(M)):
        print(M[i])
        
def init(n):
# renvoie une matrice de 0 de longueur n
    return [["0" for i in range (n)] for i in range(n)]

def bord(n):
    M = init(n+2)
    for i in range(n+2):
        M[i][0] = "."
        M[0][i] = "."
        M[len(M)-1][i] = "."
        M[i][len(M)-1] = "."
    return M

def demineur(n,m):#n = longueur matrice carre / m mines
    M = bord(n)
    M = PoserMines(M,m)
    NombreVoisin(M)
    N = initN(n)
    Perdue = False
    Gagner = False
    afficher(N)
    i = 0
    j = 0
    while (Perdue == False and Gagner == False):
        print ("Veuillez choisir une ligne et une colonne ")
        i =input("rentrer la ligne :")
        j =input("rentrer la colonne :")
        i = int(i)
        j =int(j)
        if (M[i+1][j+1] == "M"):
            print("Perdu")
            Perdue = True
            N[i][j] = M[i+1][j+1]
        else:
            N[i][j] = M[i+1][j+1]
        print("affichage de M")
        afficher(M)
        print("affichage de N")
        afficher(N)
    
    return print("return")

def PoserMines (M,m): # on pose m mines dans la matrice M, 9 =une mine
    
    while (CompterMines(M)< m):
        for i in range(len(M)):
            for j in range (len(M)):
                if (M[i][j]!="M" and M[i][j]!="."):
                    if (ProbaMine() == True):
                        M[i][j]="M"           
    return M
        
def CompterMines(M): #On compte le nombre de mines
    compteur = 0
    for i in range(len(M)-1):
        for j in range (len(M)-1):
            if (M[i][j]=="M"):
                compteur +=1
    return compteur

def ProbaMine():# sur une case donnée on a 1/100 de chance d avoir une mine
    proba = 1
    if (random.randint(1,100)<=proba):
        return True
    return False

def NombreVoisin(M):
    for i in range (1,len(M)-1): ## On ne veut pas compter les voisins de la bordure
        for j in range (1,len(M)-1):
            if (M[i][j]!="M"):      # si la case n est pas une mine
                nbVoisin =0
                if (M[i+1][j]!="."):    # si la case adjacente n est pas un bord
                    if (M[i+1][j]=="M"):    # si la case est une mine +1
                        nbVoisin +=1
                        
                if (M[i-1][j]!="."):
                    if (M[i-1][j]=="M"):
                        nbVoisin +=1
                        
                if (M[i+1][j+1]!="."):
                    if (M[i+1][j+1]=="M"):
                        nbVoisin +=1
                        
                if (M[i-1][j-1]!="."):
                    if (M[i-1][j-1]=="M"):
                        nbVoisin +=1
                        
                if (M[i][j+1]!="."):
                    if (M[i][j+1]=="M"):
                        nbVoisin +=1
                        
                if (M[i][j-1]!="."):
                    if (M[i][j-1]=="M"):
                        nbVoisin +=1
                        
                if (M[i+1][j-1]!="."):
                    if (M[i+1][j-1]=="M"):
                        nbVoisin +=1
                        
                if (M[i-1][j+1]!="."):
                    if (M[i-1][j+1]=="M"):
                        nbVoisin +=1
                M[i][j] =str(nbVoisin)
    return 0
            
def initN(n):
# renvoie une matrice de 0 de longueur n
    return [["?" for i in range (n)] for i in range(n)]

            
    
