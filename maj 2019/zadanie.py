file = open("przyklad.txt").read().splitlines()


#print(file)
def silnia(num):
    result=1
    for n in range(1, num):
        result=result*(n+1)
    return result


def zadanie_1():
    result=0
    for number in file:
        for j in range(0,15):
            if 3**j==int(number):
                result+=1
    return result


def zadanie_2():
    results = []
    for number in file:
        r = 0
        for num in number:
            r+=silnia(int(num))
        if r==int(number):
            results.append(r)
    return results
print(zadanie_2())