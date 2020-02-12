import random


def arrayGenerator():
    a = []
#    lenght = random.randint(1, pow(10,5))
#    print(lenght)
    for i in range(20):
        a.append(random.randint(1,5))
    return a


def firstDuplicate(a):
    dicc = {}
    limite = len(a)
    for i in range(len(a)):
        if i < limite:
            for j in range(len(a)):
                if i < j:
                    if a[i] not in dicc:
                        if a[i] == a[j]:
                            limite = j
                            dicc[a[i]] = j
                    else:
                        break
                else:
                    break
        else:
            break
    duplicados = list(dicc.keys())
    if len(duplicados) > 0:
        menor = dicc[duplicados[0]]
        for i in range(len(duplicados)):
            if i > 0:
                if menor > dicc[duplicados[i]]:
                    menor = dicc[duplicados[i]]
        return a[menor]
    else:
        return -1



a = arrayGenerator()
print(a)
print(firstDuplicate(a))
