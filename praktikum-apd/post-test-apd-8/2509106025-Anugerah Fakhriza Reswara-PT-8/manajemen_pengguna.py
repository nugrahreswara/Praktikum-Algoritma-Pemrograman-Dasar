from data_pengguna import pengguna
from validasi import validasi_email, validasi_umur

def tambah_pengguna(username, password, nama_lengkap, umur, no_telp, email, role="user"):
    pengguna[username] = {
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "no_telp": no_telp,
        "email": email,
        "role": role
    }

def hapus_pengguna(username):
    if username in pengguna:
        del pengguna[username]

def perbarui_profil_pengguna(username, nama_lengkap=None, umur=None, no_telp=None, email=None, password=None):
    data = pengguna[username]
    if nama_lengkap is not None:
        data["nama_lengkap"] = nama_lengkap
    if umur is not None:
        data["umur"] = umur
    if no_telp is not None:
        data["no_telp"] = no_telp
    if email is not None:
        data["email"] = email
    if password is not None:
        data["password"] = password

def pengguna_ada(username):
    return username in pengguna

def dapatkan_data_pengguna(username):
    return pengguna.get(username)

def dapatkan_semua_pengguna():
    return pengguna
