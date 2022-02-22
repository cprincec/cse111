import random

def main():
    numbers_list = []

    print(numbers_list)

    append_random_numbers(numbers_list)
    print(numbers_list)

    append_random_numbers(numbers_list, 3)
    print(numbers_list)


def append_random_numbers(numbers_list, quantity = 1):
    
    random_num = random.uniform(1, 20)
    random_num = round(random_num, 1)
    
    numbers = numbers_list.append(random_num)
    if quantity != 1:
        for _ in range(quantity-1):
            numbers = numbers_list.append(random_num)

    return numbers

if __name__  == "__main__":
    main()