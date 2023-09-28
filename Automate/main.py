"""Headline : Automate de programmation
Objectif: Saisie et Analyse d'un texte puis son affichage
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """


#Importation des fonctions
import fonctions as f



#Saisie du texte a verifier
texte = input()

#Analyse du texte et retour en bool (True ou False)
bool = f.traitement(texte)

#Affichage du résultat
if bool:
    print('La phrase est syntaxiquement correcte')
else: 
    print('La phrase est syntaxiquement incorrecte')