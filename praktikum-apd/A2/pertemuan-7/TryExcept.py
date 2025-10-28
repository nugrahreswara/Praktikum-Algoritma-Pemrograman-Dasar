#while True:
#	try:
#		angka = int(input("Masukkan angka: "))
#		print(angka)
#	except ValueError:
#		print("Angka tidak boleh kosong")

#try:
#	angka = int(input('Masukkan Angka : '))
#
#except ValueError:
#	print('input yang anda masukkan bukan Integer (angka)')
#else :
#	print(f'Angka yang kamu input : {angka}')
#finally :
#	print('Blok Try Selesai')
#try:
#	usn = input('Username yang diinginkan : ')
#	if len(usn) < 5:
#		raise ValueError('Nama Minimal Memiliki 5 karakter')
#	print(f"Username: {usn}")
#
#except ValueError as e:
#	print(e)

while True:
	try:
		nama = input("Masukkan nama anda: ")
		if nama == "" or nama == " ": 
			print("Nama tidak boleh kosong")
		
		elif nama.isdigit():
			raise ValueError("Nama tidak boleh angka")

	except ValueError as e:
		print(e)
	
	else:
		print(f"Nama yang anda masukkan: {nama}")
		
