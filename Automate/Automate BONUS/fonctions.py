"""Headline : Automate de programmation
Objectif: Version améliorée du programme avec importation du dictionnaire d'un fichier texte
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """

# Importation de la table de Transition

from constantes import tableDeTransition 


#Extraction

def extraire():

    #chemin = input('saisir le chemin du fichier texte:') en general
    chemin = '/home/maxence.martin/TP2/TP2/Automate/Automate BONUS/Dicotest'
    
    #ouverture du fichier
    f = open(chemin,'r')

    #lecture
    texte = f.readlines()

    #Creation du dictionnaire
    dictionnaire = {}

    for i in range(len(texte)):
        # texte[i] est un str de la forme "Mot 5" on le transforme en liste ["Mot", "5"]
        sousListe = texte[i].split()

        #on forme notre dictionaire 
        dictionnaire[sousListe[0]] = int(sousListe[1])

    f.close()
    return dictionnaire

dicEntrees = extraire()

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

    

