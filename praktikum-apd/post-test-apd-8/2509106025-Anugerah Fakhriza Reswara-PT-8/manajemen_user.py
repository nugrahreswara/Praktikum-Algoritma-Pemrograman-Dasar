from data_users import users
from validasi_input import validasi_email, validasi_umur

def tambah_user(username, password, nama_lengkap, umur, no_telp, email, role="user"):
    users[username] = {
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "no_telp": no_telp,
        "email": email,
        "role": role
    }

def hapus_user(username):
    if username in users:
        del users[username]

def edit_profil(username, nama_lengkap=None, umur=None, no_telp=None, email=None, password=None):
    user = users[username]
    if nama_lengkap is not None:
        user["nama_lengkap"] = nama_lengkap
    if umur is not None:
        user["umur"] = umur
    if no_telp is not None:
        user["no_telp"] = no_telp
    if email is not None:
        user["email"] = email
    if password is not None:
        user["password"] = password

def user_ada(username):
    return username in users

def get_user(username):
    return users.get(username)

def get_all_users():
    return users
