import random

simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q = int(input('веди пароль длину пароля(веди цифрами)'))
password = ''

for i in range(q):
    password += random.choice(simbols)

print(password)