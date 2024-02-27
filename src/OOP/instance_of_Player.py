from class_Player import Player


Player.set_cls_field(10)
x = Player()
print(x.level)

Player.set_cls_field()  # will set 1 (by default)
y = Player()
print(y.level)
#y.level = 2.3  # will cause error "Must be integer"
