# Username: nugrah
# Password: 025

import os
username = "nugrah"
password = "025"
percobaan = 0
maksimal_percobaan = 5

os.system('cls' if os.name == 'nt' else 'clear')

print("Silahkan login terlebih dahulu sebelum memulai program: ")
while percobaan < maksimal_percobaan:
	input_username = input("Username: ")
	input_password = input("Password: ")

	if input_username == username and input_password == password:
		print(f"Login berhasil!\n")
		
		while True:
			print(f"==============================================\nSelamat datang di program rental mobil Nugrah.\nSilahkan pilih opsi menu dibawah:\n1. Mulai mendaftar untuk rental mobil\n2. Keluar dari program\n==============================================")
			pilihan = input("Pilih 1 - 2: ")

			if pilihan == "1":
				usia_customer = int(input("Masukkan usia customer: "))
				sim = input("Masukkan SIM: ")
				deposit = int(input("Masukkan deposit: "))
				pengalaman_mengemudi = int(input("Masukkan pengalaman mengemudi berapa tahun: "))
				if usia_customer < 21:
					print(f"===============================\nTolak: Usia tidak mencukupi\n===============================")
					print(f"===============================\nProgram selesai\n===============================")
					mengulang = input("Apakah anda ingin mengulang pendaftaran? ketik Ya untuk mengulang: ")
					if mengulang.lower() == "ya" or mengulang.lower() == "y":
						os.system('cls' if os.name == 'nt' else 'clear')
						continue
					else:
						print("Program dihentikan")
						exit()

				elif sim != "A":
					print(f"===============================\nTolak: Tidak memiliki SIM A\n===============================")
					print(f"===============================\nProgram selesai\n===============================")
					mengulang = input("Apakah anda ingin mengulang pendaftaran? ketik Ya untuk mengulang: ")
					if mengulang.lower() == "ya" or mengulang.lower() == "y":
						os.system('cls' if os.name == 'nt' else 'clear')
						continue
					else:
						print("Program dihentikan")
						exit()

				elif deposit < 500000:
					print(f"===============================\nTolak: Deposit tidak cukup\n===============================")
					print(f"===============================\nProgram selesai\n===============================")
					mengulang = input("Apakah anda ingin mengulang pendaftaran? ketik Ya untuk mengulang: ")
					if mengulang.lower() == "ya" or mengulang.lower() == "y":
						os.system('cls' if os.name == 'nt' else 'clear')
						continue
					else:
						print("Program dihentikan")
						exit()

				elif pengalaman_mengemudi < 4:
					print(f"===============================\nSetujui untuk mobil standar saja\n===============================")
					print(f"===============================\nProgram selesai\n===============================")
					mengulang = input("Apakah anda ingin mengulang pendaftaran? ketik Ya untuk mengulang: ")
					if mengulang.lower() == "ya" or mengulang.lower() == "y":
						os.system('cls' if os.name == 'nt' else 'clear')
						continue
					else:
						print("Program dihentikan")
						exit()
		
				else:
					print(f"===============================\nSetujui untuk semua jenis mobil\n===============================")
					print(f"===============================\nProgram selesai\n===============================")
					mengulang = input("Apakah anda ingin mengulang program lagi? ketik Ya untuk mengulang: ")
					if mengulang.lower() == "ya" or mengulang.lower() == "y":
						os.system('cls' if os.name == 'nt' else 'clear')
						continue
					else:
						print("Program dihentikan")
						exit()

			elif pilihan == "2":
				print("Keluar dari program...")
				exit()
			else:
				print("Pilihan tidak valid, mohon memilih angka 1 - 2")

	else:
		percobaan += 1	
		sisa_percobaan = maksimal_percobaan - percobaan
		if sisa_percobaan > 0:
			print(f"\nLogin gagal! Anda tersisa {sisa_percobaan} percobaan lagi.")
		else:
			print(f"\nPercobaan login sudah mencapai batas")
			break
print("Program akan dihentikan")
