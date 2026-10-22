from pathlib import Path

path=Path(input("Каталог: "))
extension=input("Расширение: ")
if not extension.startswith("."):
    extension="."+extension
try:
    if not path.exists():
        raise FileNotFoundError

    if not path.is_dir():
        raise NotADirectoryError
    for file in path.rglob("*"+extension):
        if file.is_file():
            print(file, file.stat().st_size, "байт")
except FileNotFoundError:
    print("Каталог не существует")
except NotADirectoryError:
    print("Указанный путь не является каталогом")
except PermissionError:
    print("Нет доступа к каталогу")
