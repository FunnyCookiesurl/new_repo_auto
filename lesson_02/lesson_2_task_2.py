def is_year_leap(year):

    return year % 4 == 0


test_years = [2020, 2008, 2009, 2023, 2024]

for year in test_years:
    result = is_year_leap(year)
    print(f"год {year}: {result}")
