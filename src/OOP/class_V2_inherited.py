from class_Verification import Verification


class V2(Verification):

    def __init__(self, login, password, age):  # 'age' exists only in here in 'V2' class.
        Verification.__init__(self, login, password)
        self.__save()
        self.age = age

    def __save(self):  # some additional functions to Parent save() method
        with open('users') as f:
            for i in f:  # i = 1 row
                if i == f"{self.login, self.password}"+"\n":
                    raise ValueError("User already exists")
        Verification.save(self)  # if user don't exist, write through calling Parent method save()

    def show(self):
        return self.login, self.password



# another example of inheritance

#from tkinter import Tk, Button

# class My_app(Tk):  # inherit 'Tk'
#
#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry("400x400")
#         self.setUI()
#
#     def setUI(self):
#         Button(self, text='OK').pack()
#
#
# root = My_app()
# root.mainloop()
