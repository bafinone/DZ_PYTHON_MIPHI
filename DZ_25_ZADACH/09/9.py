def parse_number(value):
    return float(value)


value=input("Введите число: ")

try:
    number=parse_number(value)
    print("Число:",number)

except ValueError:
    print("Некорректное значение")
