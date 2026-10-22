def read_file(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Файл не найден")

    except PermissionError:
        print("Нет прав доступа")

    except OSError:
        print("Ошибка операционной системы")


text=read_file("text.txt")

if text is not None:
    print(text)
