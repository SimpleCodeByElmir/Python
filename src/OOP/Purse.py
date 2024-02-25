# This is an implementation of a virtual wallet.


class Wallet:

    def __init__(self, currency="USD", owner="Unknown"):
        if currency not in ('USD', 'EUR', 'RUB'):
            print("Currency is not supported.\nOnly USD, EUR or RUB.")
            raise ValueError("Currency is not supported.\nOnly USD, EUR or RUB.")
        else:
            self.__money = 0.0
            self.currency = currency
            self.owner = owner

    def info(self):
        print(f"{self.__money}\n{self.currency}\n{self.owner}")

    def top_up_balance(self, amount_of_money, currency):
        if self.currency != currency:
            print(f"Choose the same currency ({currency}).")
            raise ValueError("Different currencies.")
        else:
            self.__money = self.__money + amount_of_money
        return amount_of_money

    def top_down_balance(self, amount_of_money, currency):
        if self.__money - amount_of_money < 0:
            print("Insufficient funds.\nPlease, top up your balance.")
            raise ValueError("Insufficient funds.\nPlease, top up your balance.")
        elif self.currency != currency:
            print(f"Choose the same currency ({currency}).")
            raise ValueError("Different currencies.")
        else:
            self.__money = self.__money - amount_of_money
        return amount_of_money

    def __del__(self):
        print("Object deleted.")


#x = Wallet('USD')
#y = Wallet('USD')

#x.info()
#y.info()

#x.top_up_balance(10, 'USD')
#y.top_up_balance(x.top_down_balance(6, 'USD'), 'USD')

#x.info() # 4
#y.info() # 6

