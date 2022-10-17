money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

i = money_capital

month = 0  # количество месяцев, которое можно прожить
while i >= 0:

    i += salary
    i = i - spend
    spend += spend * (increase + 1)
    month += 1

print(month)
