from constantes import DicEntrees, TableDeTransition

def SaisirTexte():
    #Fonction pour saisir une phrase qui sera renvoyée
    Texte = str(input())
    return Texte


def Traitement(Texte):

    Liste = Texte.split()
    #Cette fonction reçoit une liste de mots (str), et analyse si la phrase formée est correcte (True) ou pas (False)
    
    n = len(Liste)  #Taille Liste
    i = 0   #itérateur
    Etat = 0 #Etat Initial

    #On parcourt les mots dans une boucle qui ne s'arrête pas tant que l'état n'est pas 8 (False) ou 9 (True)
    
    while Etat < 8 and i < n:
        TypeMot = DicEntrees[Liste[i]]
        Etat = TableDeTransition[Etat][TypeMot]
        i += 1 
    
    if Etat == 9: return True
    return False 
        
     
