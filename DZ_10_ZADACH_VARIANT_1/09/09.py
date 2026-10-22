class BankAccount:
    def __init__(self,owner,balance=0):
        if balance<0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        self.owner=owner
        self.__balance=balance
        self.__history=["Открытие счета: "+str(balance)]

    def get_balance(self):
        return self.__balance

    def get_history(self):
        return self.__history.copy()

    def _add_history(self,text):
        self.__history.append(text)

    def deposit(self,amount):
        if amount<=0:
            self._add_history("Отказ пополнения: "+str(amount))
            raise ValueError("Сумма должна быть положительной")

        self.__balance+=amount
        self._add_history("Пополнение: "+str(amount))

        return self.__balance

    def _withdraw_money(self,amount):
        self.__balance-=amount
        self._add_history("Снятие: "+str(amount))

        return self.__balance

    def withdraw(self,amount):
        if amount<=0:
            self._add_history("Отказ снятия: "+str(amount))
            raise ValueError("Сумма должна быть положительной")

        if amount>self.__balance:
            self._add_history("Отказ снятия: недостаточно средств")
            raise ValueError("Недостаточно средств")

        return self._withdraw_money(amount)


class SavingsAccount(BankAccount):
    def __init__(self,owner,balance=0,minimum_balance=100):
        super().__init__(owner,balance)
        self.minimum_balance=minimum_balance

    def withdraw(self,amount):
        if amount>0 and self.get_balance()-amount<self.minimum_balance:
            self._add_history("Отказ снятия: минимальный остаток")
            raise ValueError("Нельзя снизить баланс ниже минимального остатка")

        return super().withdraw(amount)


class CreditAccount(BankAccount):
    def __init__(self,owner,balance=0,credit_limit=500):
        super().__init__(owner,balance)
        self.credit_limit=credit_limit

    def withdraw(self,amount):
        if amount<=0:
            self._add_history("Отказ снятия: "+str(amount))
            raise ValueError("Сумма должна быть положительной")

        if self.get_balance()-amount < -self.credit_limit:
            self._add_history("Отказ снятия: превышен кредитный лимит")
            raise ValueError("Превышен кредитный лимит")

        return self._withdraw_money(amount)


accounts=[
    BankAccount("Иван",1000),
    SavingsAccount("Мария",1000,200),
    CreditAccount("Олег",100,1500)
]

for account in accounts:
    print("\nВладелец:",account.owner)

    try:
        account.withdraw(1200)
        print("Новый баланс:",account.get_balance())
    except ValueError as error:
        print("Ошибка:",error)

    print("История:",account.get_history())
