import os

users = {
    "admin": {
        "password": "admin123",
        "nama_lengkap": "Administrator",
        "umur": 30,
        "no_telp": "081234567890",
        "email": "admin@nugrah.my.id",
        "role": "admin"
    }
}

sudah_login = False
user_sekarang = None

def tampilkan_menu_utama():
    """Menampilkan menu saat belum login."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MANAJEMEN AKSES SERVER PENYIMPANAN ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

def tampilkan_menu_user():
    """Menampilkan menu setelah login."""
    os.system('cls' if os.name == 'nt' else 'clear')
    data_user = users[user_sekarang]
    print(f"Selamat datang, {data_user['nama_lengkap']} ({user_sekarang})")
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

def validasi_email(email):
    return "@" in email and "." in email and len(email) > 5

def validasi_umur(umur_str):
    try:
        umur = int(umur_str)
        return umur if 1 <= umur <= 150 else None
    except (ValueError, TypeError):
        return None

def login():
    """Prosedur login pengguna."""
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
            return
        else:
            percobaan += 1
            if percobaan < maks_percobaan:
                print(f"Username atau password salah. Percobaan ke-{percobaan} dari {maks_percobaan}.")
            else:
                print("Anda telah gagal login 5 kali. Program dihentikan.")
                exit()

def logout():
    """Prosedur logout pengguna."""
    global sudah_login, user_sekarang
    sudah_login = False
    user_sekarang = None
    print("Anda telah logout.")
    input("Tekan Enter untuk kembali...")

while True:
    if not sudah_login:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            login()
        elif pilihan == "2":
            print("\n=== REGISTRASI USER BARU ===")
            username_baru = input("Masukkan username baru: ").strip()
            if not username_baru:
                print("Username tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
            if username_baru in users:
                print("Username sudah digunakan.")
                input("Tekan Enter untuk kembali...")
                continue

            password_baru = input("Masukkan password: ").strip()
            if not password_baru:
                print("Password tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue

            nama_lengkap = input("Nama lengkap: ").strip()
            if not nama_lengkap:
                print("Nama lengkap tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue

            umur_input = input("Umur: ").strip()
            umur = validasi_umur(umur_input)
            if umur is None:
                print("Umur harus angka antara 1–150.")
                input("Tekan Enter untuk kembali...")
                continue

            no_telp = input("Nomor telepon: ").strip()
            if not no_telp:
                print("Nomor telepon tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue

            email = input("Alamat email: ").strip()
            if not validasi_email(email):
                print("Format email tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue

            # Simpan user baru
            users[username_baru] = {
                "password": password_baru,
                "nama_lengkap": nama_lengkap,
                "umur": umur,
                "no_telp": no_telp,
                "email": email,
                "role": "user"
            }
            print("Registrasi berhasil! Silakan login.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

    else:
        tampilkan_menu_user()
        data_user = users[user_sekarang]
        pilihan = input("Pilih menu: ").strip()

        try:
            if data_user["role"] == "admin":
                if pilihan == "1":
                    print("\n=== TAMBAH USER BARU (ADMIN) ===")
                    username_baru = input("Username: ").strip()
                    if not username_baru:
                        print("Username tidak boleh kosong.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    if username_baru in users:
                        print("Username sudah digunakan.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    password_baru = input("Password: ").strip()
                    if not password_baru:
                        print("Password tidak boleh kosong.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    nama_lengkap = input("Nama lengkap: ").strip()
                    if not nama_lengkap:
                        print("Nama lengkap tidak boleh kosong.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    umur_input = input("Umur: ").strip()
                    umur = validasi_umur(umur_input)  
                    if umur is None:
                        print("Umur tidak valid.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    no_telp = input("Nomor telepon: ").strip()
                    if not no_telp:
                        print("Nomor telepon tidak boleh kosong.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    email = input("Email: ").strip()
                    if not validasi_email(email):  
                        print("Format email tidak valid.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    users[username_baru] = {
                        "password": password_baru,
                        "nama_lengkap": nama_lengkap,
                        "umur": umur,
                        "no_telp": no_telp,
                        "email": email,
                        "role": "user"
                    }
                    print("User berhasil ditambahkan.")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "2":
                    target = input("\nUsername yang akan dihapus: ").strip()
                    if target == "admin":
                        print("Tidak bisa menghapus akun admin utama.")
                    elif target not in users:
                        print("User tidak ditemukan.")
                    elif users[target]["role"] == "admin":
                        print("Tidak bisa menghapus admin lain.")
                    else:
                        del users[target]
                        print("User berhasil dihapus.")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "3":
                    print("\n=== DAFTAR USER ===")
                    for uname, data in users.items():
                        print(f"- {uname} | {data['nama_lengkap']} | {data['role']}")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "4":
                    print("\n=== EDIT PROFIL ===")
                    print("Biarkan kosong jika tidak ingin mengubah.")
                    nama_baru = input(f"Nama lengkap ({data_user['nama_lengkap']}): ").strip()
                    if nama_baru:
                        data_user["nama_lengkap"] = nama_baru

                    umur_baru = input(f"Umur ({data_user['umur']}): ").strip()
                    if umur_baru:
                        umur = validasi_umur(umur_baru)  
                        if umur is None:
                            print("Umur tidak valid.")
                        else:
                            data_user["umur"] = umur

                    telp_baru = input(f"Nomor telepon ({data_user['no_telp']}): ").strip()
                    if telp_baru:
                        data_user["no_telp"] = telp_baru

                    email_baru = input(f"Email ({data_user['email']}): ").strip()
                    if email_baru and validasi_email(email_baru):  
                        data_user["email"] = email_baru
                    elif email_baru:
                        print("Format email tidak valid.")

                    password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip()
                    if password_baru:
                        data_user["password"] = password_baru

                    print("Profil berhasil diperbarui.")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "5":
                    logout()
                elif pilihan == "6":
                    print("Terima kasih telah menggunakan program ini.")
                    break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk kembali...")

            else:  
                if pilihan == "1":
                    print("\n=== EDIT PROFIL ===")
                    print("Biarkan kosong jika tidak ingin mengubah.")
                    nama_baru = input(f"Nama lengkap ({data_user['nama_lengkap']}): ").strip()
                    if nama_baru:
                        data_user["nama_lengkap"] = nama_baru

                    umur_baru = input(f"Umur ({data_user['umur']}): ").strip()
                    if umur_baru:
                        umur = validasi_umur(umur_baru) 
                        if umur is None:
                            print("Umur tidak valid.")
                        else:
                            data_user["umur"] = umur

                    telp_baru = input(f"Nomor telepon ({data_user['no_telp']}): ").strip()
                    if telp_baru:
                        data_user["no_telp"] = telp_baru

                    email_baru = input(f"Email ({data_user['email']}): ").strip()
                    if email_baru and validasi_email(email_baru):  
                        data_user["email"] = email_baru
                    elif email_baru:
                        print("Format email tidak valid.")

                    password_baru = input("Password baru: ").strip()
                    if password_baru:
                        data_user["password"] = password_baru

                    print("Profil berhasil diperbarui.")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "2":
                    logout()
                elif pilihan == "3":
                    print("Terima kasih telah menggunakan program ini.")
                    break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk kembali...")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input("Tekan Enter untuk melanjutkan...")
