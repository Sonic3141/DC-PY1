def days():
    money_capital = 10000
    salary = 5000
    spend = 6000
    increase = 0.05
    month = 1  # количество месяцев, которое можно прожить

    while  money_capital >= 0:
       money_capital = money_capital + salary - spend

       print(money_capital, month)
       spend = spend * (increase +1)
       month += 1
       if money_capital <= 0:
            month -= 2
    return(month)

print(days())
