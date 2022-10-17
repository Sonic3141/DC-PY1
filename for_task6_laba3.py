list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_index = 0
max_el = list_numbers[max_index]

for i, current_el in enumerate(list_numbers):  # перебираем пары индекс - значение
    max_el = list_numbers[max_index]
    if current_el> max_el:  # если текущий элемент больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального
        max_el = list_numbers[max_index]  # и перезаписываем число
list_numbers[i], list_numbers[9] = list_numbers[9], list_numbers[i]
print(list_numbers)
