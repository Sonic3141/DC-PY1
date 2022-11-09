list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = 0

for i in range(len(list_numbers)): #цикл с 1 по последний элемент из заданного списка
    if list_numbers[i] > max:
        max = list_numbers[i]
        index = i
list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index] #множественное присваивание, требуемое по условию
print(list_numbers)