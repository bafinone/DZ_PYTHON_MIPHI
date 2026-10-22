from pathlib import Path

path=Path(input("Введите путь к каталогу: "))

if not path.is_dir():
    print("Каталог не существует")
else:
    files=0
    directories=0
    total_size=0

    for item in path.rglob("*"):
        if item.is_file():
            files+=1
            total_size+=item.stat().st_size

        elif item.is_dir():
            directories+=1

    print("Количество файлов:",files)
    print("Количество подкаталогов:",directories)
    print("Python-файлы:")

    for item in path.rglob("*.py"):
        print(item)

    print("Суммарный размер:",total_size)
