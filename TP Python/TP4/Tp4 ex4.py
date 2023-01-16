def element_frequent(liste):
    occurrences = {}

    for element in liste:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    element_frequent, frequence = max(occurrences.items(), key=lambda x: x[1])
    return element_frequent, frequence

ma_liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
element_le_plus_frequent, frequence = element_frequent(ma_liste)
print("L'élément le plus fréquent est: ", element_le_plus_frequent)
print("Fréquence d'apparition: ", frequence)
