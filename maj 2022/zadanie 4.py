
file=open(r"przyklad.txt")
file=file.read().splitlines()

###########Zad 4.1############

def first_last_numbers(file):
    result_numbers=[]
    for number in file:
        if number[0]==number[len(number)-1]:
            result_numbers.append(number)
    return result_numbers

results = first_last_numbers(file)
#print(len(results), results[0])

##########Zad 4.2###############

def prime_factors(number):
    div_numbers=[]
    for div_number in range(2,10000):
        while number%div_number == 0:
            div_numbers.append(div_number)
            number = number//div_number
            if number  == 1:
                return div_numbers

def prime_factors_for_numbers(file):
    prime_factors_for_num=[]
    for number in file:
        prime_factors_for_number_without_duplicates=list(dict.fromkeys(prime_factors(int(number))))
        prime_factors_for_num.append([number, len(prime_factors(int(number))), len(prime_factors_for_number_without_duplicates)])
    return prime_factors_for_num

def max_prime_factors(numbers):
    max_number_with_duplicates=[]
    max_number_without_duplicates=[]
    for number in numbers:
        if len(max_number_with_duplicates)==0 or number[1]>max_number_with_duplicates[1]:
            max_number_with_duplicates=number
        if len(max_number_without_duplicates)==0 or number[2]>max_number_without_duplicates[2]:
            max_number_without_duplicates=number
    max_number_with_duplicates.pop(2)
    max_number_without_duplicates.pop(1)
    return max_number_with_duplicates, max_number_without_duplicates

#print(max_prime_factors(prime_factors_for_numbers(file)))

################Zad 4.3#################


def search_divable_number(number,file):
    for num in file:
        if int(num)%int(number)==0 and int(num)!=number:
            return int(num)
    return None
            
good_5=[]
good_3=[]
for number in file:
    numbers=[]
    divider=int(number)
    numbers.append(divider)
    while True:
        next_number=search_divable_number(divider, file)
        print(next_number)
        if next_number!=None:
            numbers.append(next_number)
            divider=next_number
        elif len(numbers)==3:
            good_3.append(numbers)
            break
        elif len(numbers)==5:
            good_5.append(numbers)
            break
        else:
            break
        
        
            
print(good_5)
print(good_3)