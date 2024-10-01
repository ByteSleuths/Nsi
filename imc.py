def imc(poids: float, taille: float) -> float:
    """
    Calcule l'Indice de Masse Corporelle (IMC) à partir du poids (en kg) et de la taille (en mètres).

    L'IMC est défini par la formule :
        IMC = poids / (taille ** 2)

    Un IMC entre 18.5 et 24.9 est considéré comme normal.
    Un IMC inférieur à 18.5 est considéré comme insuffisance pondérale.
    Un IMC supérieur à 24.9 est considéré comme surpoids.

    :param poids: Poids de la personne en kilogrammes (float)
    :param taille: Taille de la personne en mètres (float)
    :return: L'IMC de la personne (float)
    
    
    Exemple:
    >>> imc(70, 1.75)
    22.86
    
    >>> imc(95, 1.80)
    29.32
    """
    if poids <= 0 or taille <= 0:
        raise ValueError("Le poids et la taille doivent être supérieurs à 0.")
    
    return round(poids / (taille ** 2), 2)


print(imc(62, 1.80))  
print(imc(95, 1.80))  
    

