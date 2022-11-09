def get_unique_list_numbers() -> list[int]:
    import random
    lis = random.sample(range(-10, 10), 15)#заполнение списка 15ю случайными уникальными числами в диапазоне от -10 до 10
    return lis

list_unique_numbers = []
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

