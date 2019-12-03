def pendu(mot):
    essai =10
    while (essai>0):
        print("Essayez de deviner le mot ou une occurence, sachant que le mot fait "+str((len(mot)))+" lettres de longeur")
        print("Il vous reste "+str(essai) + " tentatives")
    
        saisi = str(input())
        if trouverMot(mot,saisi) == True:
            print ("Bravo vous avez trouvé le mot "+ mot)
            return 1
        if (Foccurence (mot ,saisi) != "0,[]"):
            print ("Voici le nb d occurence(s) et leur(s) position(s) ")
            print (Foccurence(mot,saisi))
        essai = essai -1
    
        
def Foccurence (mot, lettre):
    occurence = 0
    position = []
    for i in range (len(mot)):
        if (mot[i] == lettre):
            occurence = occurence +1
            position.append(i+1)
    return occurence, position
def trouverMot (Vraimot,mot):
    for i in range (len(Vraimot)):
        try:
            if (mot[i] != Vraimot[i]):
                return False
        except:
            return False
        
    return True

    
    

        
