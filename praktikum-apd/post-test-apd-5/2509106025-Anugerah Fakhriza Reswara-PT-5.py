import os

users = [
    ["admin", "admin123", "Administrator", 30, "081234567890", "admin@nugrah.com", "admin"]
]

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
                user_ditemukan = None
                for user in users:
                    if user[0] == username and user[1] == password:
                        user_ditemukan = user
                        break
                
                if user_ditemukan is not None:
                    sudah_login = True
                    user_sekarang = user_ditemukan
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
            username_ada = False
            for user in users:
                if user[0] == username_baru:
                    username_ada = True
                    break
            
            if username_ada:
                print("Username sudah digunakan. Silakan pilih username lain.")
                input("Tekan Enter untuk kembali...")
            else:
                password_baru = input("Masukkan password: ").strip()
                nama_lengkap = input("Nama lengkap: ").strip()
                
                umur_input = input("Umur: ").strip()
                if umur_input.isdigit():
                    umur = int(umur_input)
                else:
                    print("Umur harus berupa angka. Registrasi dibatalkan.")
                    input("Tekan Enter untuk kembali...")
                    continue
                
                no_telp = input("Nomor telepon: ").strip()
                email = input("Alamat email: ").strip()
                
                users.append([username_baru, password_baru, nama_lengkap, umur, no_telp, email, "user"])
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
        print(f"Selamat datang, {user_sekarang[2]} ({user_sekarang[0]})")
        if user_sekarang[6] == "admin":
            print("Anda adalah admin.")
        else:
            print("Anda memiliki akses ke server penyimpanan.")
        
        print("\n=== MENU ===")
        if user_sekarang[6] == "admin":
            print("1. Tambah User")
            print("2. Hapus User")
            print("3. Lihat Daftar User")
            print("4. Edit Profil")
            print("5. Logout")
            print("6. Keluar")
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == "1":
                print("\n=== TAMBAH USER BARU (ADMIN) ===")
                username_baru = input("Username: ").strip()
                username_ada = False
                for user in users:
                    if user[0] == username_baru:
                        username_ada = True
                        break
                
                if username_ada:
                    print("Username sudah digunakan.")
                else:
                    password_baru = input("Password: ").strip()
                    nama_lengkap = input("Nama lengkap: ").strip()
                    
                    umur_input = input("Umur: ").strip()
                    if umur_input.isdigit():
                        umur = int(umur_input)
                    else:
                        print("Umur harus angka.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    no_telp = input("Nomor telepon: ").strip()
                    email = input("Email: ").strip()
                    
                    users.append([username_baru, password_baru, nama_lengkap, umur, no_telp, email, "user"])
                    print("User berhasil ditambahkan.")
                input("Tekan Enter untuk kembali...")
                continue
            
            elif pilihan == "2":
                print("\n=== HAPUS USER ===")
                target_user = input("Masukkan username yang akan dihapus: ").strip()
                
                if target_user == "admin":
                    print("Tidak bisa menghapus akun admin utama.")
                else:
                    user_dihapus = False
                    for i in range(len(users)):
                        if users[i][0] == target_user:
                            if users[i][6] == "admin":
                                print("Tidak bisa menghapus akun admin lain.")
                            else:
                                del users[i]
                                user_dihapus = True
                                print("User berhasil dihapus.")
                            break
                    if not user_dihapus:
                        print("User tidak ditemukan.")
                input("Tekan Enter untuk kembali...")
                continue
            
            elif pilihan == "3":
                print("\n=== DAFTAR USER ===")
                for user in users:
                    print(f"- {user[0]} | {user[2]} | {user[6]}")
                input("Tekan Enter untuk kembali...")
                continue
            
            elif pilihan == "4":
                pass
            elif pilihan == "5":
                pass
            elif pilihan == "6":
                pass
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
        
        else:
            print("1. Edit Profil")
            print("2. Logout")
            print("3. Keluar")
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == "1":
                pass
            elif pilihan == "2":
                pass
            elif pilihan == "3":
                pass
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
        
        if pilihan == "4" or (user_sekarang[6] != "admin" and pilihan == "1"):
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            
            nama_baru = input(f"Nama lengkap ({user_sekarang[2]}): ").strip()
            if nama_baru != "":
                user_sekarang[2] = nama_baru
            
            umur_baru = input(f"Umur ({user_sekarang[3]}): ").strip()
            if umur_baru != "":
                if umur_baru.isdigit():
                    user_sekarang[3] = int(umur_baru)
                else:
                    print("Umur harus angka. Perubahan umur dibatalkan.")
            
            telp_baru = input(f"Nomor telepon ({user_sekarang[4]}): ").strip()
            if telp_baru != "":
                user_sekarang[4] = telp_baru
            
            email_baru = input(f"Email ({user_sekarang[5]}): ").strip()
            if email_baru != "":
                user_sekarang[5] = email_baru
            
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip()
            if password_baru != "":
                user_sekarang[1] = password_baru
            
            print("Profil berhasil diperbarui.")
            input("Tekan Enter untuk kembali...")
        
        elif pilihan == "5" or (user_sekarang[6] != "admin" and pilihan == "2"):
            sudah_login = False
            user_sekarang = None
            print("Anda telah logout.")
            input("Tekan Enter untuk kembali...")
        
        elif pilihan == "6" or (user_sekarang[6] != "admin" and pilihan == "3"):
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
