file=open("duplikaty.txt")
file=file.read().splitlines()


array=[]
for x in file:
    array.append(x)

def remove_duplicates(array):
    for number in array:
        if array.count(number)>1:
            array.remove(number)
    return array

print(remove_duplicates(array))


def missing_numbers(array):
    numbers=[]
    for number in range(0,100):
        if array.count(number)>=1:
            continue
        numbers.append(number)
    return numbers

print(missing_numbers(array))