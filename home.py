class Money:

    def __init__(self, rub, proc):
        self.rub = rub
        self.proc = proc

    def get_count(self):
        self.rub = str(self.rub)
        x = self.rub.split('.')
        return print(f'У вас есть {x[:-1]}  рублей и {x[1:]}  копеек')

class Good(Money):

    def get_tovar(self):
        self.rub = float(self.rub)
        itog = float((self.rub - ((self.rub * self.proc) / 100)))
        if self.proc > 100 or self.proc <= 0:
            print('Не правильный процент')
        else:
            print(f'Общая сумма = {self.rub} руб, '
                  f'процент от этой суммы = {((self.rub * self.proc) / 100)} За товар: {itog}')




sum = Good(150.00, 35)
sum.get_count()
sum.get_tovar()



# a = 7.76
# txt = str(a)
# x = txt.split('.')
# print(x[:-1]) #7
# print(x[1:])  #76