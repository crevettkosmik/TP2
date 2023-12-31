"""Headline : Automate de programmation
Objectif: Dictionnaire et Table de Transition de l'automate
Date: 28/09/2023
BELBACHIR Yassine & MARTIN Maxence
To do: None """
 

#Dictionnaire
dicEntrees = {"le" : 0, 
              "la" : 0, 
              "chat" : 2, 
              "souris" : 2, 
              "martin" : 4,
              "mange" : 3, 
              "une" : 0, 
              "petite" : 1, 
              "joli" : 1, 
              "grosse" : 1,
              "bleu" : 1, 
              "verte" : 1, 
              "dort" : 3,
              "julie" : 4,
              "jean" : 4, 
              "." : 5 } 

tableDeTransition = ((1, 8, 8, 8, 4, 8),
                     (8, 1, 2, 8, 8, 8),
                     (8, 2, 8, 3, 8, 8),
                     (5, 0, 0, 0, 7, 9),
                     (8, 8, 8, 3, 8, 8),
                     (8, 5, 6, 8, 8, 8),
                     (8, 6, 8, 8, 8, 9),
                     (8, 8, 8, 8, 8, 9))