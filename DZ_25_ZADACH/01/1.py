with open("text.txt","r",encoding="utf-8") as file:
    lines=0
    words=0
    chars=0
    maxline=0
    for line in file:
        lines+=1
        words+=len(line.split())
        chars+=len(line)
        maxline=max(maxline,len(line.rstrip("\n")))
print("Количество строк:",lines)
print("Количество слов:",words)
print("Количество символов:",chars)
print("Длина самой длинной строки:",maxline)
