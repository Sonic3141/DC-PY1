salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
procent = spend
while (months !=1 ):

    procent = procent * (increase +1)
    spend += procent
    months -= 1

need_money = spend - salary *10
print(round(need_money))
