import os
import time


spisok = []
for adress, dirs, files in os.walk('C://Users/user/Desktop/FL about'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)


print(spisok)
