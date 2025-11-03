from autentikasi import login, logout, is_logged_in, get_current_user
from tampilan import tampilkan_menu_utama, tampilkan_menu_user, tampilkan_daftar_user
from manajemen_user import (
    tambah_user, hapus_user, edit_profil,
    user_ada, get_user, get_all_users
)
from validasi_input import validasi_email, validasi_umur
from data_users import users
import sys

def registrasi():
    print("\n=== REGISTRASI USER BARU ===")
    username_baru = input("Masukkan username baru: ").strip()
    if not username_baru:
        print("Username tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return

    if user_ada(username_baru):
        print("Username sudah digunakan.")
        input("Tekan Enter untuk kembali...")
        return

    password_baru = input("Masukkan password: ").strip()
    if not password_baru:
        print("Password tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return

    nama_lengkap = input("Nama lengkap: ").strip()
    if not nama_lengkap:
        print("Nama lengkap tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return

    umur = validasi_umur(input("Umur: ").strip())
    if umur is None:
        print("Umur harus angka antara 1–150.")
        input("Tekan Enter untuk kembali...")
        return

    no_telp = input("Nomor telepon: ").strip()
    if not no_telp:
        print("Nomor telepon tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return

    email = input("Alamat email: ").strip()
    if not validasi_email(email):
        print("Format email tidak valid.")
        input("Tekan Enter untuk kembali...")
        return

    tambah_user(username_baru, password_baru, nama_lengkap, umur, no_telp, email, "user")
    print("Registrasi berhasil! Silakan login.")
    input("Tekan Enter untuk kembali...")

def menu_user_biasa():
    current = get_current_user()
    data_user = get_user(current)
    while True:
        tampilkan_menu_user()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input(f"Nama lengkap ({data_user['nama_lengkap']}): ").strip() or None
            umur_baru_str = input(f"Umur ({data_user['umur']}): ").strip()
            umur_baru = validasi_umur(umur_baru_str) if umur_baru_str else None
            if umur_baru_str and umur_baru is None:
                print("Umur tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            telp_baru = input(f"Nomor telepon ({data_user['no_telp']}): ").strip() or None
            email_baru = input(f"Email ({data_user['email']}): ").strip() or None
            if email_baru and not validasi_email(email_baru):
                print("Format email tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip() or None

            edit_profil(current, nama_baru, umur_baru, telp_baru, email_baru, password_baru)
            print("Profil berhasil diperbarui.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            logout()
            break
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            sys.exit()
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

def menu_admin():
    current = get_current_user()
    while True:
        tampilkan_menu_user()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            print("\n=== TAMBAH USER BARU (ADMIN) ===")
            username_baru = input("Username: ").strip()
            if not username_baru:
                print("Username tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
            if user_ada(username_baru):
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

            umur = validasi_umur(input("Umur: ").strip())
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

            tambah_user(username_baru, password_baru, nama_lengkap, umur, no_telp, email, "user")
            print("User berhasil ditambahkan.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            target = input("\nUsername yang akan dihapus: ").strip()
            if target == "admin":
                print("Tidak bisa menghapus akun admin utama.")
            elif not user_ada(target):
                print("User tidak ditemukan.")
            elif get_user(target)["role"] == "admin":
                print("Tidak bisa menghapus admin lain.")
            else:
                hapus_user(target)
                print("User berhasil dihapus.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            tampilkan_daftar_user()

        elif pilihan == "4":
            data_user = get_user(current)
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input(f"Nama lengkap ({data_user['nama_lengkap']}): ").strip() or None
            umur_baru_str = input(f"Umur ({data_user['umur']}): ").strip()
            umur_baru = validasi_umur(umur_baru_str) if umur_baru_str else None
            if umur_baru_str and umur_baru is None:
                print("Umur tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            telp_baru = input(f"Nomor telepon ({data_user['no_telp']}): ").strip() or None
            email_baru = input(f"Email ({data_user['email']}): ").strip() or None
            if email_baru and not validasi_email(email_baru):
                print("Format email tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip() or None

            edit_profil(current, nama_baru, umur_baru, telp_baru, email_baru, password_baru)
            print("Profil berhasil diperbarui.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            logout()
            break
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini.")
            sys.exit()
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    while True:
        if not is_logged_in():
            tampilkan_menu_utama()
            pilihan = input("Pilih menu (1/2/3): ").strip()
            if pilihan == "1":
                login()
            elif pilihan == "2":
                registrasi()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk kembali...")
        else:
            current = get_current_user()
            role = get_user(current)["role"]
            if role == "admin":
                menu_admin()
            else:
                menu_user_biasa()
