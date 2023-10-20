salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total = 0
money_capital = 0
for i in range(10):
    total = total + spend
    price_up = spend * increase
    spend = spend + price_up
    money_capital = total - (salary * months)
money_capital = round(money_capital, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",money_capital)
