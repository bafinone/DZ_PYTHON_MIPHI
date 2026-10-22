from contextlib import contextmanager


@contextmanager
def log_operation(filename,operation):
    with open(filename,"a",encoding="utf-8") as file:
        file.write("START: "+operation+"\n")

        try:
            yield

        except Exception:
            file.write("ERROR: "+operation+"\n")
            raise

        else:
            file.write("END: "+operation+"\n")


with log_operation("operation.log","Data processing"):
    print("Обработка данных")
