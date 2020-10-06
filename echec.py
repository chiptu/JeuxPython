def afficher(M):
# affiche la matrice
    for i in range(len(M)):
        print(M[i])
        
def init(n):
# renvoie une matrice de 0 de longueur n
    return [["0" for i in range (n)] for i in range(n)]

# Objet piece (param equipe, pour prise+ appel fct echec?)
#pour determiner mouvement?


def bord():
    M = init(9)
    for i in range(9):
        M[0][0] = "?"
        M[1][0] = "A"
        M[2][0] = "B"
        M[3][0] = "C"
        M[4][0] = "D"
        M[5][0] = "E"
        M[6][0] = "F"
        M[7][0] = "G"
        M[8][0] = "H"
        
        M[0][0] = "?"
        M[0][1] = "1"
        M[0][2] = "2"
        M[0][3] = "3"
        M[0][4] = "4"
        M[0][5] = "5"
        M[0][6] = "6"
        M[0][7] = "7"
        M[0][8] = "8"
        
    return M

def debut():
    M = bord()
    M[1][1] = "T"
    M[1][2] = "C"
    M[1][3] = "F"
    M[1][4] = "Q"
    M[1][5] = "K"
    M[1][6] = "F"
    M[1][7] = "C"
    M[1][8] = "T"

    M[2][1] = "z"
    M[2][2] = "z"
    M[2][3] = "z"
    M[2][4] = "z"
    M[2][5] = "z"
    M[2][6] = "z"
    M[2][7] = "z"
    M[2][8] = "z"

    M[8][1] = "t"
    M[8][2] = "c"
    M[8][3] = "f"
    M[8][4] = "q"
    M[8][5] = "k"
    M[8][6] = "f"
    M[8][7] = "c"
    M[8][8] = "t"

    M[7][1] = "p"
    M[7][2] = "p"
    M[7][3] = "p"
    M[7][4] = "p"
    M[7][5] = "p"
    M[7][6] = "p"
    M[7][7] = "p"
    M[7][8] = "p"

    return M
    
    

def echec():
    
    M = debut()
    
    afficher(M)
    
    
