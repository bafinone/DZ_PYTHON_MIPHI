class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance,amount):
    if amount<=0:
        raise InvalidAmountError("Некорректная сумма")

    if amount>balance:
        raise InsufficientFundsError("Недостаточно денег")

    return balance-amount


balance=1000
amount=float(input("Сколько снять: "))

try:
    balance=withdraw(balance,amount)
    print("Новый баланс:",balance)

except InvalidAmountError as error:
    print(error)

except InsufficientFundsError as error:
    print(error)
