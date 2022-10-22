file = open("przyklad.txt")
file = file.read().splitlines()


def list_to_int(array):
    number=""
    for x in array:
        number+=x
    return int(number)

def prime_number_check(number):
    divisors=[]
    for num in range(1,number+1):
        if number%num==0:
            divisors.append(num)
    if sum(divisors)==number+1:
        return True
    return False

def zadanie_4_1(file):
    result=[]
    for number in file:
        number=list(number)
        number.reverse()
        number=list_to_int(number)
        if number%17==0:
            result.append(number)
    return result

def zadanie_4_2(file):
    result={}
    for number in file:
        number_reversed=list(number)
        number_reversed.reverse()
        number2=list_to_int(list(number))-list_to_int(number_reversed)
        if number2<0:
            number2=abs(number2)
        result.update({number: number2})
    return result

def zadanie_4_3(file):
    numbers=[]
    for number in file:
        number_reversed=list(number)
        number_reversed.reverse()
        if prime_number_check(list_to_int(number_reversed))==True and prime_number_check(list_to_int(list(number)))==True:
            numbers.append(number)
    return numbers

def zadanie_4_4(file):
    unique_numbers=[]
    numbers_2=[]
    numbers_3=[]
    for number in file:
        if unique_numbers.count(number)!=1:
            unique_numbers.append(number)
            continue
        if file.count(number)==2:
            numbers_2.append(number)
        if file.count(number)==3:
            numbers_3.append(number)
    
    return len(unique_numbers), len(numbers_2), len(numbers_3)

print("Zadanie 4.1:\n", zadanie_4_1(file))
print("Zadanie 4.2:\n",max(zadanie_4_2(file), key=zadanie_4_2(file).get), zadanie_4_2(file)[max(zadanie_4_2(file), key=zadanie_4_2(file).get)])
print("Zadanie 4.3:\n", zadanie_4_3(file))

print("Zadanie 4.4: \n",zadanie_4_4(file))
