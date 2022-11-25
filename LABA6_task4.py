import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename: str, delimiter=',', newline='\n') -> list[dict]:#Реализовать конвертер из csv в json

    with open(filename, encoding='utf-8') as f: #открытие файла
        data = []
        for el in f: #разделение на элементы в файле
            data.append([i.rstrip(newline) for i in el.split(delimiter)])
    dic = [] #итоговый список
    for i in range(1, len(data)):
        new_dict = {}#словарь для каждой строки
        for k in range(len(data[0])):
            new_dict.update({data[0][k]: data[i][k]})

        dic + new_dict # добавление в итоговый список
    return dic

print(json.dumps(csv_to_list_dict(INPUT_FILE)), indent=4, ensure_ascii=False) #на всякий случай, чтобы русский текст тоже читался