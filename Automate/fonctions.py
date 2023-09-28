"""Headline : Automate de programmation
Objectif: Fonctions de Saisie et Analyse d'un texte puis de son affichage
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """

# Importation du Dictionnaire et de la table de Transition

from constantes import dicEntrees, tableDeTransition 

# Analyse Syntaxique

def traitement(texte):
    #Cette fonction reçoit une liste de mots (str), et analyse si la phrase formée est correcte (True) ou pas (False)
    
    #Conversion du texte entré en liste de str
    liste = texte.split()
    
    
    #Initialisation
    n = len(liste)  #Taille Liste
    i = 0   #itérateur associé aux mots de la liste
    etat = 0 #Etat Initial

    #On parcourt les mots dans une boucle qui ne s'arrête pas tant que l'état n'est pas 8 (False) ou 9 (True) ou si l'itérateur déborde
    
    while etat < 8 and i < n:
        typeMot = dicEntrees[liste[i]]
        etat = tableDeTransition[etat][typeMot]
        i += 1 
    
    #renvoi de la validité de la phrase en bool
    if etat == 9: return True
    return False 



        
     
