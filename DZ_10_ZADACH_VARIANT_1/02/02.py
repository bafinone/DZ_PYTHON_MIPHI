def unusual_string():
    best_string=""
    best_count=-1
    while True:
        text=input("Введите строку (STOP для завершения): ")
        if text.upper()=="STOP":
            break
        count=len(set(text.lower()))
        if count>best_count:
            best_string=text
            best_count=count
    if best_count==-1:
        print("Строки не введены")
    else:
        print("Самая необычная строка:",best_string)
        print("Количество различных символов:",best_count)


unusual_string()
