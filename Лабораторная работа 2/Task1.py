money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
total_money = money_capital + salary - 6000
while total_money >= 0:
    price_up = spend * increase
    spend = price_up + spend
    spend = round(spend, 2)
    total_money = total_money + salary
    total_money = total_money - spend
    month = month + 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
