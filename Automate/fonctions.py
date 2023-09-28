"""Headline : Automate de programmation
Objectif: Fonctions de Saisie et Analyse d'un texte puis de son affichage
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """

# Importation du Dictionnaire et de la table de Transition
from constantes import DicEntrees, TableDeTransition 

# Acquisition d’une phrase
def SaisirTexte():
    #Fonction pour saisir une phrase qui sera renvoyée
    
    Texte = str(input())
    return Texte

# Analyse Syntaxique
def Traitement(Texte):
    #Cette fonction reçoit une liste de mots (str), et analyse si la phrase formée est correcte (True) ou pas (False)
    
    #Conversion du texte entré en liste de str
    Liste = Texte.split()
    
    
    #Initialisation
    n = len(Liste)  #Taille Liste
    i = 0   #itérateur associé aux mots de la liste
    Etat = 0 #Etat Initial

    #On parcourt les mots dans une boucle qui ne s'arrête pas tant que l'état n'est pas 8 (False) ou 9 (True) ou si l'itérateur déborde
    
    while Etat < 8 and i < n:
        TypeMot = DicEntrees[Liste[i]]
        Etat = TableDeTransition[Etat][TypeMot]
        i += 1 
    
    #renvoi de la validité de la phrase en bool
    if Etat == 9: return True
    return False 

#Affichage du résultat : phrase correcte ou non
def Resultat(Bool):
    if Bool: return print('La phrase est syntaxiquement correcte')
    return print('La phrase est syntaxiquement incorrecte')

        
     
