usia_customer = int(input("Masukkan usia customer: "))

sim = input("Masukkan SIM: ")

deposit = int(input("Masukkan deposit: "))

pengalaman_mengemudi = int(input("Masukkan pengalaman mengemudi berapa tahun: "))

if usia_customer < 21:
	print("Tolak: Usia tidak mencukupi")

elif sim != "A":
	print("Tolak: Tidak memiliki SIM A")

elif deposit < 500000:
	print("Tolak: Deposit tidak cukup")

elif pengalaman_mengemudi < 4:
	print("Setujui untuk mobil standar saja")

else:
	print("Setujui untuk semua jenis mobil")
