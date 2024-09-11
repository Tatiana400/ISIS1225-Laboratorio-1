def two_sum(lst, target):
    """
    Verificar si existe al menos un par de números en la lista lst, tal que sumados sean igual al número target.

    :param lst: lista de enteros, con mínimo 2 elementos.
    :type lst: dict (representando una lista array_list)
    :param target: Número objetivo
    :type target: int

    return True si existe tal pareja, False de lo contrario.
    """
    existe = False
    n1 = 0
    n2 = 0
    for i in range(len(lst)):
        n1 = lst[i]
        if (target-n1) in lst:
            existe = True
        else:
            existe

    return existe

l = [1, 4, 8, 10, 6] 
t = 13
print(two_sum(l,t))


