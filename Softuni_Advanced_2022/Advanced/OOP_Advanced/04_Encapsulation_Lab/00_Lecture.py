class CreditCard:
    def __init__(self, number: str, name: str, cvv: str, expr_date: str, pin: str):
        self.number = number
        self.name = name
        self.cvv = cvv
        self.expr_date = expr_date
        self.__pin = pin # this attribute is private


mastercard = CreditCard('0120391023912930', 'Test name', '123', '2023-11', '0000')

mastercard.name = 'Test_2'

print(mastercard.name)

print(mastercard._CreditCard__pin) 