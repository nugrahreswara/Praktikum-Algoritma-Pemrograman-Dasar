import random
from datetime import datetime

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""

for i in range(1, 12):
	kata_sandi += random.choice(karakter)
print(kata_sandi)

print(datetime.now())
