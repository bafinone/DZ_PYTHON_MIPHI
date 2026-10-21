with open("numbers.txt","r",encoding="utf-8") as file:
    total=0
    count=0
    minimum=None
    maximum=None

    for line in file:
        line=line.strip()
        if not line:
            continue
        try:
            number=int(line)
        except ValueError:
            print("Ошибка: строка не является числом:",line)
            continue
        total+=number
        count+=1
        if minimum is None or number<minimum:
            minimum=number
        if maximum is None or number>maximum:
            maximum=number
with open("result.txt","w",encoding="utf-8") as file:
    if count==0:
        file.write("Корректных чисел нет\n")
    else:
        average=total/count
        file.write("Минимум: "+str(minimum)+"\n")
        file.write("Максимум: "+str(maximum)+"\n")
        file.write("Среднее: "+str(average)+"\n")
