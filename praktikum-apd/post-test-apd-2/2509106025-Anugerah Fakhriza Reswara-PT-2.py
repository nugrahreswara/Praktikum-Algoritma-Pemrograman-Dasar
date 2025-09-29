nama = str(input("Masukkan nama anda: "))
umur = int(input("Masukkan umur anda: "))
tinggi_badan = int(input("Masukkan tinggi badan anda: "))
berat_badan = float(input("Masukkan berat badan anda: "))
status = bool(input("Apakah anda mahasiswa aktif? Kosongkan jika tidak: "))

print(f"""====== Biodata ======
Nama: {nama}
Umur: {umur}
Tinggi badan: {tinggi_badan}
Berat badan: {berat_badan}
Status keaktifan: {status}
====================
""")
