# Polymorphism. Multiple inheritance.

class A:
    def n(self):
        print("A")

class B:
    def n(self):
        print('B')

class C(B):
    def n(self):
        print('C')

class D(C, A):
    def n(self):
        super().n()  # as we see comment below, super() will find 'n()' method in class 'C'
        print(self.__class__.__mro__)  # (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>,
                                       # <class '__main__.A'>, <class 'object'>)
                                       # notice, that we will search in deep, not in wide,
                                       # so it will look like D-C-B-A, and not like D-C-A-B

    # or, if we need to call certain 'n()' from certain Parent
    def z(self):
        super(B, self).n()  # but if we need to print A, we put B. Coz it works like this - linearized. Starts from X.


D().n()  # 'C'. Because method 'super' first finds Parent 'C'.
print()

# see the searching path of super()
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>,
                  # <class '__main__.A'>, <class 'object'>)

print()
D().z()  # A