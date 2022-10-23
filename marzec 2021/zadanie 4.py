file = open("galerie_przyklad.txt")
file = file.read().splitlines()


def get_countries(file):
    countries=[]
    for element in file:
        country=''
        for char in element:
            if char==' ' and countries.count(country)==0:
                countries.append(country)
            if char!=' ':
                country+=char
            else:
                break
    return countries

def zadanie_4_1(file):
    countries= get_countries(file)
    result={}
    for element in file:
        for country in countries:
            if element.startswith(country) and element[len(country)]==" " and result.get(country)==None:
                result.update({country:1})
            elif element.startswith(country) and element[len(country)]==" ":
                result[country]+=1
    return result

def zadanie_4_2(file):
    result={}
    for element in file: 
        info= element.split(" ")
        town = info[1]
        lokale=0
        gallery_area=0
        for i in range(2, len(element), 2):
            if info[i]=='0':
                break
            lokale+=1
            lokal_area=int(info[i])*int(info[i+1])
            gallery_area+=lokal_area
        result.update({town : [gallery_area,lokale]})
    return result
#print(zadanie_4_1(file))
print(zadanie_4_2(file))
print(max(zadanie_4_2(file), key=zadanie_4_2(file).get), zadanie_4_2(file)[max(zadanie_4_2(file), key=zadanie_4_2(file).get)])
print(min(zadanie_4_2(file), key=zadanie_4_2(file).get), zadanie_4_2(file)[max(zadanie_4_2(file), key=zadanie_4_2(file).get)])
