file = open("przyklad.txt")
file = file.read().splitlines()


def zadanie_4_1(file):
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    result = 0
    for element in file:
        for chara in element:
            if chara in numbers:
                result += 1
    return result


def zadanie_4_2(file):
    index = 20
    pos = 1
    result = ""
    while index <= 1000:
        result += file[index - 1][pos - 1]
        index += 20
        pos += 1
    return result


def zadanie_4_3(file):
    result = ""
    for element in file:
        option_1 = element + element[0]
        option_2 = element[len(element) - 1] + element
        if option_1 == option_1[::-1]:
            result += option_1[25]
        elif option_2 == option_2[::-1]:
            result += option_2[25]
    return result


def zadanie_4_4(file):
    result = ""
    for element in file:
        num_1 = -1
        num_2 = -1
        for char in element:
            if char.isdigit() and num_1 == -1:
                num_1 = char
            elif char.isdigit():
                num_2 = char
                ascii = num_1 + num_2
                if int(ascii) >= 65 and int(ascii) <= 90:
                    result += chr(int(ascii))
                num_1 = -1
                num_2 = -1
        if result.endswith("XXX"):
            break
    return result


print("Zadanie 4.1:\n", zadanie_4_1(file))
print("Zadanie 4.2:\n", zadanie_4_2(file))
print("Zadanie 4.3:\n", zadanie_4_3(file))
print("Zadanie 4.4:\n", zadanie_4_4(file))
