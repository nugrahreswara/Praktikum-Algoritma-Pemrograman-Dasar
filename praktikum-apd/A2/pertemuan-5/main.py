# Membuat list
#matakuliah = ["APD", "Kalkulus", "Orsikom"]
#print(matakuliah[1:3])
#print(matakuliah[-1])
#print(matakuliah[1:3:2])

#matakuliah1 = []
#matakuliah1.append("Matematika Diskrit")
#print (matakuliah1)
# Studi kasus
#keranjang = ["Brokoli", "Apel", "Jamur", "Nanas", "Wortel", "Kiwi", "Kol", "Sawi", "Lobak"]

#matakuliah.append("Matematika Diskrit")
#matakuliah.insert(-1, "Jaringan Komputer")
#print(matakuliah)

#praktikum = ["Mahasiswa", 20, True, 45.10, ["APD", 25]]
#print(praktikum[4][0])

#studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
#studyclub[2] = "Web"
#print(studyclub)


#matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
#hapus = matakuliah.pop(3)
#print(matakuliah)
#print(matakuliah)
#del matakuliah[2]
#matakuliah.remove("Kalkulus")
#matakuliah.pop()
#matakuliah.pop(2)
#print(matakuliah)

#List = [1, 2, 3]
#Nilai = [4, 5, 6]
#Hasil = list + nilai
#Kali = list * 3
#Print(hasil)
#Print(kali)
#print(len(list))
#print(max(list))
#print(average(list))

#matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
#for index, i in enumerate(matakuliah):
#	print(index, i)
#for i in matakuliah:
#	print(i)

kelas = [
["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"],
["Pernanda", "Riyadi", "Ahnaf"],
]
print(kelas[0])
print("Yang namanya Lian:",kelas[0][1])
kelas[1].insert(1, "Bakil")
print(kelas[1])
for i in kelas:
	for nama in i:
		print(nama)
