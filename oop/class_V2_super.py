from class_Verification import Verification


class V2(Verification):

    def __init__(self, login, password, age):  # 'age' exists only in here in 'V2' class.
        super().__init__(login, password)  # super() calls Parent class. And no need 'self' parameter
        self.__save()
        self.age = age

    def __save(self):  # some additional functionality in Parents save() method
        with open('users') as f:
            for i in f:  # i = 1 row
                if i == f"{self.login, self.password}"+"\n":
                    raise ValueError("User already exists")
        super().save()  # if user don't exist, write through Parents save() method

    def show(self):
        return self.login, self.password


#x = V2("Billy", "123456789", 21)
