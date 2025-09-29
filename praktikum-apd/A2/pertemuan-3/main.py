#angka = 5
#
#if angka > 5:
#	print ("angka lebih besar 5")
#
#angka = ""
#
#if angka :
#	print("Berhasil")
#
#cuaca = "hujan"
#
#if cuaca == "hujan":
#	print("Dirumah aja")
#else :
#	print("Nongkrong")
#
#nilai = 70
#if nilai >= 70:
#	print("Lulus")
#else:
#	print("Remedi")
#
#cuaca = 'mendung'
#
#if cuaca == 'hujan':
#	print("Dirumah aja")
#elif cuaca == 'mendung':
#	print('Makan mie')
#else:
#	print('Nongkrong')
#
#usia = int(input("Masukkan usia anda : "))
#if usia <= 13:
#	print("Anak-anak")
#elif usia <= 18:
#	print("Remaja")
#elif usia <= 40:
#	print("Dewasa")
#else:
#	print("Tua")
#
#
#Nilai = int(input("Masukkan nilai anda : "))
#if Nilai >= 90:
#	print("A")
#elif Nilai >= 70:
#	print("B")
#elif Nilai >= 60:
#	print("C")
#else:
#	print("D")
#
#a = 111
#b = 55
#c = 56
#
#if a < b:
#        if a < c:
#            print("a paling kecil")
#        else:
#            print("c lebih kecil dari a")
#
#elif a < c:
#    print("c lebih besar")
#
#else:
#    print("c paling besar")
#
# STUDI KASUS 1
#tinggi_badan = int(input("Masukkan tinggi badan anda: "))
#bolehgak = "Boleh menaiki wahana" if tinggi_badan >= 145 else "Tidak boleh menaiki wahana"
#print(bolehgak)

# STUDI KASUS 2
#total_belanja = int(input("Masukkan total belanja anda: "))
#if total_belanja > 100000:
#    print("Diskon 20%")
#elif total_belanja > 50000:
#    print("Diskon 10%")
#else:
#    print("Tidak mendapatkan diskon")

#total_belanja = int(input("Masukkan total belanja anda: "))
#diskon = "Diskon 20%" if total_belanja > 100000 else "Tidak mendapatkan diskon" elif total_belanja > 50000

nilai = int(input("Masukkan nilai: "))
kelas = input("Masukkan kelas: ")
if nilai >= 80 and kelas == "A":
    print("IPK 4")
elif nilai >= 80 and kelas == "B":
    print("IPK 3")
else:
    print("IPK 2")
