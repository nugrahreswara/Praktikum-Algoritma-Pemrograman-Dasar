import os
from prettytable import PrettyTable
from data_pengguna import pengguna
from autentikasi import dapatkan_pengguna_sekarang

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_utama():
    bersihkan_layar()
    print("=== MANAJEMEN AKSES SERVER PENYIMPANAN ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

def tampilkan_menu_pengguna():
    bersihkan_layar()
    username = dapatkan_pengguna_sekarang()
    data = pengguna[username]
    print(f"Selamat datang, {data['nama_lengkap']} ({username})")
    if data["role"] == "admin":
        print("Anda adalah admin.")
    else:
        print("Anda memiliki akses ke server penyimpanan.")
    print("\n=== MENU ===")
    if data["role"] == "admin":
        print("1. Tambah Pengguna")
        print("2. Hapus Pengguna")
        print("3. Lihat Daftar Pengguna")
        print("4. Edit Profil")
        print("5. Logout")
        print("6. Keluar")
    else:
        print("1. Edit Profil")
        print("2. Logout")
        print("3. Keluar")

def tampilkan_daftar_pengguna():
    tabel = PrettyTable()
    tabel.field_names = ["Username", "Nama Lengkap", "Umur", "No. Telp", "Email", "Role"]
    for uname, data in pengguna.items():
        tabel.add_row([
            uname,
            data["nama_lengkap"],
            data["umur"],
            data["no_telp"],
            data["email"],
            data["role"]
        ])
    print("\n=== DAFTAR PENGGUNA ===")
    print(tabel)
    input("Tekan Enter untuk kembali...")
