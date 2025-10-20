# Membuat set
#buah = {"apel", "jeruk", "mangga", "apel"}
#buah = (["apel", "jeruk", "mangga", "apel"])
#print (buah)

#angka_ganjil = {1, 3, 5, 7, 9}
#for angka in angka_ganjil:
#	print(angka)

#Daftar_buku = {
#	"Buku1" : "Bumi Manusia",
#	"Buku2" : "Laut Bercerita"
#}
#
#print(Daftar_buku["Buku1"])
#print(Daftar_buku)
#Biodata = {
#"Nama" : "Anugerah Fakhriza Reswara",
#"NIM" : 2509106025,
#"KRS" : ["Pemrograman Web", "Struktur Data", "Jarkom Lanjut"],
#"Mahasiswa_Aktif" : True,
#"Social Media" : {
#	"Instagram" : "@nugrahreswara"
#	}
#}
#print(f"Biodata: {Biodata['Nama']}")
#print(f"Sosial Media: {Biodata['Social Media']['Instagram']}")
#print(Biodata.get("Nama"))
Nilai = {
	"Matematika": 80,
	"B. Indonesia": 90,
	"B. Inggris": 81,
	"Kimia": 78,
	"Fisika": 80
}
#
## Tanpa menggunakan items()
for i in Nilai:
	print(i)
	print("")
#
## Menggunakan items()
for i, j in Nilai.items():
	print(f"Nilai {i} anda adalah {j}")
#Film = {
#	"Avenger Endgame" : "Action",
#	"Sherlock Holmes" : "Mystery",
#	"The Conjuring" : "Horror"
#}
#
##Sebelum Ditambah
#print(f"Sebelum ditambah: \n{Film}")
#Film["Zombieland"] = "Comedy"
#Film.update({"Hours" : "Thriller"})
#print()
##Setelah Ditambah
#print(f"Sesudah ditambah: \n{Film}")
#Film = {
#	"Avenger Endgame" : "Action",
#	"Sherlock Holmes" : "Mystery",
#	"The Conjuring" : "Horror"
#}
#
##Sebelum Diubah
#print(f"Sebelum diubah: \n{Film}")
#
#print()
#
#Film["Sherlock Holmes"] = "Action"
#Film.update({"The Conjuring" : "Tragedy"})
#
##Setelah diubah
#print(f"Setelah diubah: \n{Film}")
#data = {
#"Nama" : "Nugrah",
#"Umur" : 18,
#"Jurusan" : "Informatika"
#}
##Sebelum Dihapus
#print(data)
#del data["Nama"]
##Setelah diubah
#print(data)
#
#print(data.get("Nama"))
#data = {
#	"Nama" : "Nugrah",
#	"Umur" : 18,
#	"Jurusan" : "Informatika"
#}
#
##Sebelum Dihapus
#print(data)
#cache = data.pop("Nama")
##Setelah dihapus
#print(data)
##memanggil data yang telah dihapus pada dictionary
#print(data.get("Nama"))
##memanggil data yang telah dihapus pada variabel cache
#print(cache)

#Musik = {
#	"The Chainsmoker" : ["All we Know", "The Paris"],
#	"Alan Walker" : ["Alone", "Lily"],
#	"Neffex" : ["Best of Me", "Memories"]
#}
#
#for i, j in Musik.items():
#	print("")
#	print(f"Musik milik {i} adalah : ")
#
#	for song in j:
#		print(song)
#
