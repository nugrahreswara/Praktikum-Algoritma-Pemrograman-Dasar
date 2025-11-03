import os
from prettytable import PrettyTable
from data_users import users
from autentikasi import get_current_user

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_utama():
    clear_screen()
    print("=== MANAJEMEN AKSES SERVER PENYIMPANAN ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

def tampilkan_menu_user():
    clear_screen()
    username = get_current_user()
    data_user = users[username]
    print(f"Selamat datang, {data_user['nama_lengkap']} ({username})")
    if data_user["role"] == "admin":
        print("Anda adalah admin.")
    else:
        print("Anda memiliki akses ke server penyimpanan.")
    print("\n=== MENU ===")
    if data_user["role"] == "admin":
        print("1. Tambah User")
        print("2. Hapus User")
        print("3. Lihat Daftar User")
        print("4. Edit Profil")
        print("5. Logout")
        print("6. Keluar")
    else:
        print("1. Edit Profil")
        print("2. Logout")
        print("3. Keluar")

def tampilkan_daftar_user():
    table = PrettyTable()
    table.field_names = ["Username", "Nama Lengkap", "Umur", "No. Telp", "Email", "Role"]
    for uname, data in users.items():
        table.add_row([
            uname,
            data["nama_lengkap"],
            data["umur"],
            data["no_telp"],
            data["email"],
            data["role"]
        ])
    print("\n=== DAFTAR USER ===")
    print(table)
    input("Tekan Enter untuk kembali...")
