import random


def arrayGenerator():
    a = []
    lenght = random.randint(1, pow(10,5))
    for i in range(lenght):
        a.append(random.randint(1, lenght))
    return a


def firstDuplicate(a):
    dicc = {}
    for i in range(len(a)):
        if a[i] in dicc:
            return a[i]
        else:
            dicc[a[i]] = i
    return -1

a = arrayGenerator()
print(firstDuplicate(a))
