"""exercice asciiart encodage"""
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    cc=[s[0]]
    o = [1]
    for c in s[1:] :
        if c == cc[-1] :
            o[-1] +=1
        else :
            o.append(1)
            cc.append(c)
    return list(zip(cc,o))



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    if s =='':
        return []
    # recherche nombre de caractères identiques au premier
    premier = s[0]
    o=1
    i=1
    imax = len(s)-1
    while (i<=imax and s[i] == premier) :
        o+=1
        i+=1
    # appel récursif
    if i >imax:
        return [(premier,o)]+artcode_r('')
    return [(premier,o)]+artcode_r(s[i:])


#### Fonction principale


def main():
    """fct main"""
    print(artcode_i("KKKXWMMMMMMMMMMMMMMMMM"))
    print(artcode_r("KKKXWMMMMMMMMMMMMMMMMM"))

if __name__ == "__main__":
    main()
