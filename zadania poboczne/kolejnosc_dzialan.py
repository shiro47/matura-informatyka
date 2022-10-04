file=open("kolejnosc_dzialan.txt")
file=file.read().splitlines()

def exmpl_divider(example):
    numbers=[]
    signs=[]
    for char in example:
        try:
            numbers.append(int(char))
        except ValueError:
            signs.append(char)
    return numbers,signs

def calculate_example(example):
    data=exmpl_divider(example)
    operation=[]
    for count,number in enumerate(data[0]):
        if count==0:
            prev_number=number
            operator=data[1][data[0].index(number)]
            operation.append(number)
            operation.append(operator)
            continue
        operation.append(number)
        if operator=="+":
            prev_number=prev_number+number
        elif operator=="-":
            prev_number=prev_number-number
        try:
            operator=data[1][data[0].index(number)]
            operation.append(operator)
        except IndexError:
            break
    return prev_number, operation

for example in file:
    data=calculate_example(example)
    print(f"{' '.join(map(str, data[1]))} = {data[0]}")