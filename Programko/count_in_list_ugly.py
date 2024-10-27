"""TODO: Chce po uživateli zadat dvě skupiny čísel, poté zkoumá, kolik každé číslo z 2. skupiny (v mém kódu divisors) dělí čísel z 1. skupiny beze zbytku. Vrátí výstup zapsaný podobně jako struktura dictionary"""

# first ask user how many numbers he wants to input, then proceeds to ask him for these numbers one by one
# We will be checking if these numbers are divisible by numbers we get in get_divisors()
def get_numbers_to_be_divided():
    how_many_nums = int(input())
    numbers = []
    # ask user n times for a number
    for _ in range(how_many_nums):
        numbers.append(int(input()))

    return numbers

# does the same thing as first function but here we get the divisors we check divisibility of the first numbers with
def get_divisors():
    how_many_nums = int(input())
    numbers = []

    for _ in range(how_many_nums):
        numbers.append(int(input()))

    return numbers

numbers = get_numbers_to_be_divided()
divisors = get_divisors()

def get_divisible_numbers_count():
    div_count = []

    # loops thru divisors
    for i in range(len(divisors)):
        count = 0
        # loops thru numbers
        for j in range(len(numbers)):
            # for each divisor, we are checking how many numbers it can divide, 
            if numbers[j] % divisors[i] == 0: 
                count += 1
        
        # adds the number and count of how many numbers it divides to the list
        div_count.append(count)

    return div_count

a = get_divisible_numbers_count()

for i in range(len(divisors)):
    print(f"{divisors[i]}: {a[i]}")
