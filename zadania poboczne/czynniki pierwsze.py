 
 
 
def prime_factors(number):
    for div_number in range(2,1000):
        while number%div_number == 0:
            print(f"{number} | {div_number}")
            number = number//div_number
            if number  == 1:
                print(f'{number} | ')
                return

prime_factors(130)