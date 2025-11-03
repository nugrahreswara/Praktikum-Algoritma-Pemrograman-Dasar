import sys
from data_users import users

sudah_login = False
user_sekarang = None

def login():
    global sudah_login, user_sekarang
    maks_percobaan = 5
    percobaan = 0
    while percobaan < maks_percobaan:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        if username in users and users[username]["password"] == password:
            sudah_login = True
            user_sekarang = username
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
    global sudah_login, user_sekarang
    sudah_login = False
    user_sekarang = None
    print("Anda telah logout.")
    input("Tekan Enter untuk kembali...")

def is_logged_in():
    return sudah_login

def get_current_user():
    return user_sekarang
