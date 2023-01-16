def element_frequent(liste):
    element_frequent = None
    frequence = 0
    for element in set(liste):
        count = liste.count(element)
        if count > frequence:
            frequence = count
            element_frequent = element
    return element_frequent, frequence

ma_liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
element_le_plus_frequent, frequence = element_frequent(ma_liste)
print("L'élément le plus fréquent est: ", element_le_plus_frequent)
print("Fréquence d'apparition: ", frequence)
