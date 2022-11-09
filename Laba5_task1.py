from pprint import pprint

dic = {'bin': None, 'dec': None, 'hex': None, 'oct': None } #создание словаря с заданными ключами
sp = [] #итоговый список, который будет вмещать словари
for i in range(0,16): #от 1 до 15 по условию
    dic.update({'bin': bin(i),'dec': i,'hex': hex(i), 'oct': oct(i)})#заполнение i-го словаря (передача значений по ключам)
    sp.append(dic.copy()) #добавление словарей в итоговый список
pprint(sp) #красивый вывод списка со словарями
