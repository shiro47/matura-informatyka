file = open('mecz.txt')
file = file.read().splitlines()
file = file[0]


def zadanie_1(file):
    result=0
    for num in range(0,len(file)):
        try:
            if file[num]!=file[num+1]:
                result+=1
        except: 
            pass
    return result
        
def zadanie_2(file):
    pass

def zadanie_3(file):
    passa=0
    results=[]
    for num in range(0,len(file)):
        try:
            if file[num]==file[num+1]:
                passa+=1
                continue
            if passa+1>=10:
                results.append([file[num],passa+1])
                passa=0
            else:
                passa=0
        except:
            pass
    return results


print(zadanie_1(file))

print(zadanie_3(file))