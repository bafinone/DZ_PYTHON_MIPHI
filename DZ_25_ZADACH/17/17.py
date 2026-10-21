with open("numbers.txt","r",encoding="utf-8") as file:
    total=0
    count=0
    minimum=None
    maximum=None

    for line in file:
        line=line.strip()

        if not line:
            continue

        number=int(line)

        total+=number
        count+=1

        if minimum is None or number<minimum:
            minimum=number

        if maximum is None or number>maximum:
            maximum=number

if count==0:
    print("Чисел нет")
else:
    average=total/count

    print("Сумма:",total)
    print("Минимум:",minimum)
    print("Максимум:",maximum)
    print("Количество:",count)
    print("Среднее:",average)
