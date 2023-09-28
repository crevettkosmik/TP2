"""Headline : Automate de programmation
Objectif: Saisie et Analyse d'un texte puis son affichage
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """


#Importation des fonctions
import fonctions as f



#Saisie du texte a verifier
Texte = f.SaisirTexte()

#Analyse du texte et retour en bool (True ou False)
Bool = f.Traitement(Texte)

#Affichage du résultat
f.Resultat(Bool)