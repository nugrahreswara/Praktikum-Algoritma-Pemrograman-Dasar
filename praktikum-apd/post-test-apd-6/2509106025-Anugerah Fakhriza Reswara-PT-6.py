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

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if not sudah_login:
        print("=== MANAJEMEN AKSES SERVER PENYIMPANAN ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()
        
        if pilihan == "1":
            maks_percobaan = 5
            percobaan = 0
            berhasil_login = False
            
            while percobaan < maks_percobaan and not berhasil_login:
                username = input("Masukkan username: ").strip()
                password = input("Masukkan password: ").strip()
                
                if username in users and users[username]["password"] == password:
                    sudah_login = True
                    user_sekarang = username
                    berhasil_login = True
                    print("Login berhasil!")
                    input("Tekan Enter untuk melanjutkan...")
                else:
                    percobaan += 1
                    if percobaan < maks_percobaan:
                        print(f"Username atau password salah. Percobaan ke-{percobaan} dari 5.")
                    else:
                        print("Anda telah gagal login 5 kali. Program dihentikan.")
                        exit()
        
        elif pilihan == "2":
            print("\n=== REGISTRASI USER BARU ===")
            username_baru = input("Masukkan username baru: ").strip()
            
            if username_baru == "":
                print("Username tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
                
            if username_baru in users:
                print("Username sudah digunakan. Silakan pilih username lain.")
                input("Tekan Enter untuk kembali...")
            else:
                password_baru = input("Masukkan password: ").strip()
                if password_baru == "":
                    print("Password tidak boleh kosong.")
                    input("Tekan Enter untuk kembali...")
                    continue
                    
                nama_lengkap = input("Nama lengkap: ").strip()
                if nama_lengkap == "":
                    print("Nama lengkap tidak boleh kosong.")
                    input("Tekan Enter untuk kembali...")
                    continue
                
                umur_input = input("Umur: ").strip()
                if umur_input.isdigit():
                    umur = int(umur_input)
                    if umur < 1 or umur > 150:
                        print("Umur tidak valid.")
                        input("Tekan Enter untuk kembali...")
                        continue
                else:
                    print("Umur harus berupa angka. Registrasi dibatalkan.")
                    input("Tekan Enter untuk kembali...")
                    continue
                
                no_telp = input("Nomor telepon: ").strip()
                if no_telp == "":
                    print("Nomor telepon tidak boleh kosong.")
                    input("Tekan Enter untuk kembali...")
                    continue
                
                email = input("Alamat email: ").strip()
                if "@" not in email or "." not in email:
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
                print("Registrasi berhasil! Silakan login.")
                input("Tekan Enter untuk kembali...")
        
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
    
    else:
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
            pilihan = input("Pilih menu: ").strip()
        else:
            print("1. Edit Profil")
            print("2. Logout")
            print("3. Keluar")
            pilihan = input("Pilih menu: ").strip()
        
        if (data_user["role"] == "admin" and pilihan == "4") or (data_user["role"] != "admin" and pilihan == "1"):
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            
            nama_baru = input(f"Nama lengkap ({data_user['nama_lengkap']}): ").strip()
            if nama_baru != "":
                if nama_baru == "":
                    print("Nama lengkap tidak boleh kosong.")
                else:
                    data_user["nama_lengkap"] = nama_baru
            
            umur_baru = input(f"Umur ({data_user['umur']}): ").strip()
            if umur_baru != "":
                if umur_baru.isdigit():
                    umur = int(umur_baru)
                    if umur < 1 or umur > 150:
                        print("Umur tidak valid. Perubahan dibatalkan.")
                    else:
                        data_user["umur"] = umur
                else:
                    print("Umur harus angka. Perubahan umur dibatalkan.")
            
            telp_baru = input(f"Nomor telepon ({data_user['no_telp']}): ").strip()
            if telp_baru != "":
                if telp_baru == "":
                    print("Nomor telepon tidak boleh kosong.")
                else:
                    data_user["no_telp"] = telp_baru
            
            email_baru = input(f"Email ({data_user['email']}): ").strip()
            if email_baru != "":
                if "@" not in email_baru or "." not in email_baru:
                    print("Format email tidak valid. Perubahan dibatalkan.")
                else:
                    data_user["email"] = email_baru
            
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip()
            if password_baru != "":
                if password_baru == "":
                    print("Password tidak boleh kosong.")
                else:
                    data_user["password"] = password_baru
            
            print("Profil berhasil diperbarui.")
            input("Tekan Enter untuk kembali...")
            continue
        
        elif (data_user["role"] == "admin" and pilihan == "5") or (data_user["role"] != "admin" and pilihan == "2"):
            sudah_login = False
            user_sekarang = None
            print("Anda telah logout.")
            input("Tekan Enter untuk kembali...")
            continue
        
        elif (data_user["role"] == "admin" and pilihan == "6") or (data_user["role"] != "admin" and pilihan == "3"):
            print("Terima kasih telah menggunakan program ini.")
            break
        
        elif data_user["role"] == "admin" and pilihan == "1":
            print("\n=== TAMBAH USER BARU (ADMIN) ===")
            username_baru = input("Username: ").strip()
            if username_baru == "":
                print("Username tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
            if username_baru in users:
                print("Username sudah digunakan.")
                input("Tekan Enter untuk kembali...")
                continue
                
            password_baru = input("Password: ").strip()
            if password_baru == "":
                print("Password tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
                
            nama_lengkap = input("Nama lengkap: ").strip()
            if nama_lengkap == "":
                print("Nama lengkap tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
            
            umur_input = input("Umur: ").strip()
            if umur_input.isdigit():
                umur = int(umur_input)
                if umur < 1 or umur > 150:
                    print("Umur tidak valid.")
                    input("Tekan Enter untuk kembali...")
                    continue
            else:
                print("Umur harus angka.")
                input("Tekan Enter untuk kembali...")
                continue
            
            no_telp = input("Nomor telepon: ").strip()
            if no_telp == "":
                print("Nomor telepon tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
                
            email = input("Email: ").strip()
            if "@" not in email or "." not in email:
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
            continue
        
        elif data_user["role"] == "admin" and pilihan == "2":
            print("\n=== HAPUS USER ===")
            target_user = input("Masukkan username yang akan dihapus: ").strip()
            
            if target_user == "admin":
                print("Tidak bisa menghapus akun admin utama.")
            elif target_user not in users:
                print("User tidak ditemukan.")
            elif users[target_user]["role"] == "admin":
                print("Tidak bisa menghapus akun admin lain.")
            else:
                del users[target_user]
                print("User berhasil dihapus.")
            input("Tekan Enter untuk kembali...")
            continue
        
        elif data_user["role"] == "admin" and pilihan == "3":
            print("\n=== DAFTAR USER ===")
            for uname, data in users.items():
                print(f"- {uname} | {data['nama_lengkap']} | {data['role']}")
            input("Tekan Enter untuk kembali...")
            continue
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
            continue
