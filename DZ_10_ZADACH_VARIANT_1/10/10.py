from functools import wraps


def log_command(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Выполнение команды")

        try:
            result=func(*args,**kwargs)
            print("Команда выполнена")
            return result
        except Exception as error:
            print("Ошибка выполнения:",error)
            raise

    return wrapper


class Command:
    def execute(self,current,value):
        raise NotImplementedError


class AddCommand(Command):
    def execute(self,current,value):
        return current+value


class MultiplyCommand(Command):
    def execute(self,current,value):
        return current*value


class SubtractCommand(Command):
    def execute(self,current,value):
        return current-value


class DivideCommand(Command):
    def execute(self,current,value):
        if value==0:
            raise ZeroDivisionError("Делить на ноль нельзя")

        return current/value


class CommandProcessor:
    def __init__(self):
        self.value=0
        self.history=[]

        self.commands={
            "add":AddCommand(),
            "multiply":MultiplyCommand(),
            "subtract":SubtractCommand(),
            "divide":DivideCommand()
        }

    @log_command
    def execute_command(self,name,number):
        if name not in self.commands:
            raise ValueError("Неизвестная команда")

        old_value=self.value
        command=self.commands[name]
        self.value=command.execute(self.value,number)

        self.history.append(
            name+" "+str(number)+": "+str(old_value)+" -> "+str(self.value)
        )

        return self.value

    def show_history(self):
        if len(self.history)==0:
            print("История пуста")
        else:
            for item in self.history:
                print(item)


processor=CommandProcessor()

while True:
    text=input("Команда: ").strip().lower()

    if text=="exit":
        break

    if text=="history":
        processor.show_history()
        continue

    parts=text.split()

    if len(parts)!=2:
        print("Введите команду и число, например: add 15")
        continue

    name=parts[0]

    try:
        number=float(parts[1])
        result=processor.execute_command(name,number)
        print("Текущий результат:",result)

    except ValueError as error:
        print("Ошибка:",error)

    except ZeroDivisionError as error:
        print("Ошибка:",error)
