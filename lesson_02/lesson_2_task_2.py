def is_year_leap(year):
    return True if year % 4 == 0 else False


n = int(input("Введите год"))
result = is_year_leap(n)
print("Год", n, ":", result)
