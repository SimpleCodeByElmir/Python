# Implementation of some element of a Verification process.

class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()  # calling this method when creating an object

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError("password is too weak")

    def save(self):
        with open('users', 'a') as f:
            f.write(f"{self.login, self.password}"+"\n")
