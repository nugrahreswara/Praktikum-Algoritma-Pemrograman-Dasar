import sys
from data_pengguna import pengguna

_sudah_login = False
_pengguna_sekarang = None

def login():
    global _sudah_login, _pengguna_sekarang
    maks_percobaan = 5
    percobaan = 0
    while percobaan < maks_percobaan:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        if username in pengguna and pengguna[username]["password"] == password:
            _sudah_login = True
            _pengguna_sekarang = username
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return True
        else:
            percobaan += 1
            if percobaan < maks_percobaan:
                print(f"Username atau password salah. Percobaan ke-{percobaan} dari {maks_percobaan}.")
            else:
                print("Anda telah gagal login 5 kali. Program dihentikan.")
                sys.exit()
    return False

def logout():
    global _sudah_login, _pengguna_sekarang
    _sudah_login = False
    _pengguna_sekarang = None
    print("Anda telah logout.")
    input("Tekan Enter untuk kembali...")

def sudah_login():
    return _sudah_login

def dapatkan_pengguna_sekarang():
    return _pengguna_sekarang
