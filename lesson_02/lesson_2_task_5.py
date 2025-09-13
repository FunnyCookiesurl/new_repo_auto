def month_to_season(number_month):
    if number_month in [12, 1, 2]:
        return "Зима"
    elif number_month in [3, 4, 5]:
        return "Весна"
    elif number_month in [6, 7, 8]:
        return "Лето"
    elif number_month in [9, 10, 11]:
        return "Осень"
    else:
        return "Название сезона"


number_month = int(input("Введите номер месяца (1-12): "))
print("Сезон:", month_to_season(number_month))
