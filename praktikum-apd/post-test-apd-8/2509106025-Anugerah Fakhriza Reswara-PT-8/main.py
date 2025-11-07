from autentikasi import login, logout, sudah_login, dapatkan_pengguna_sekarang
from antarmuka import tampilkan_menu_utama, tampilkan_menu_pengguna, tampilkan_daftar_pengguna, bersihkan_layar
from manajemen_pengguna import (
    tambah_pengguna, hapus_pengguna, perbarui_profil_pengguna,
    pengguna_ada, dapatkan_data_pengguna, dapatkan_semua_pengguna
)
from validasi import validasi_email, validasi_umur
from data_pengguna import pengguna
import sys

def daftar_pengguna_baru():
    print("\n=== REGISTRASI PENGGUNA BARU ===")
    username = input("Masukkan username baru: ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return
    if pengguna_ada(username):
        print("Username sudah digunakan.")
        input("Tekan Enter untuk kembali...")
        return

    password = input("Masukkan password: ").strip()
    if not password:
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

    tambah_pengguna(username, password, nama_lengkap, umur, no_telp, email, "user")
    print("Registrasi berhasil! Silakan login.")
    input("Tekan Enter untuk kembali...")

def menu_pengguna_biasa():
    username = dapatkan_pengguna_sekarang()
    data = dapatkan_data_pengguna(username)
    while True:
        tampilkan_menu_pengguna()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input(f"Nama lengkap ({data['nama_lengkap']}): ").strip() or None
            teks_umur = input(f"Umur ({data['umur']}): ").strip()
            umur_baru = validasi_umur(teks_umur) if teks_umur else None
            if teks_umur and umur_baru is None:
                print("Umur tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            telp_baru = input(f"Nomor telepon ({data['no_telp']}): ").strip() or None
            email_baru = input(f"Email ({data['email']}): ").strip() or None
            if email_baru and not validasi_email(email_baru):
                print("Format email tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip() or None

            perbarui_profil_pengguna(username, nama_baru, umur_baru, telp_baru, email_baru, password_baru)
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
    username = dapatkan_pengguna_sekarang()
    while True:
        tampilkan_menu_pengguna()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":  # Tambah pengguna
            print("\n=== TAMBAH PENGGUNA BARU (ADMIN) ===")
            username_baru = input("Username: ").strip()
            if not username_baru:
                print("Username tidak boleh kosong.")
                input("Tekan Enter untuk kembali...")
                continue
            if pengguna_ada(username_baru):
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

            tambah_pengguna(username_baru, password_baru, nama_lengkap, umur, no_telp, email, "user")
            print("Pengguna berhasil ditambahkan.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":  # Hapus pengguna
            target = input("\nUsername yang akan dihapus: ").strip()
            if target == "admin":
                print("Tidak bisa menghapus akun admin utama.")
            elif not pengguna_ada(target):
                print("Pengguna tidak ditemukan.")
            elif dapatkan_data_pengguna(target)["role"] == "admin":
                print("Tidak bisa menghapus admin lain.")
            else:
                hapus_pengguna(target)
                print("Pengguna berhasil dihapus.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":  # Lihat daftar
            tampilkan_daftar_pengguna()

        elif pilihan == "4":  # Edit profil
            data = dapatkan_data_pengguna(username)
            print("\n=== EDIT PROFIL ===")
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input(f"Nama lengkap ({data['nama_lengkap']}): ").strip() or None
            teks_umur = input(f"Umur ({data['umur']}): ").strip()
            umur_baru = validasi_umur(teks_umur) if teks_umur else None
            if teks_umur and umur_baru is None:
                print("Umur tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            telp_baru = input(f"Nomor telepon ({data['no_telp']}): ").strip() or None
            email_baru = input(f"Email ({data['email']}): ").strip() or None
            if email_baru and not validasi_email(email_baru):
                print("Format email tidak valid.")
                input("Tekan Enter untuk kembali...")
                continue
            password_baru = input("Password baru (kosongkan jika tidak ingin ganti): ").strip() or None

            perbarui_profil_pengguna(username, nama_baru, umur_baru, telp_baru, email_baru, password_baru)
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

# Program Utama
if __name__ == "__main__":
    while True:
        if not sudah_login():
            tampilkan_menu_utama()
            pilihan = input("Pilih menu (1/2/3): ").strip()
            if pilihan == "1":
                login()
            elif pilihan == "2":
                daftar_pengguna_baru()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk kembali...")
        else:
            username = dapatkan_pengguna_sekarang()
            role = dapatkan_data_pengguna(username)["role"]
            if role == "admin":
                menu_admin()
            else:
                menu_pengguna_biasa()
