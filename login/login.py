from ui_utils import line, text_centered, text_left
import re
from database.user import check_user, create_user

def login_screen():
    isLoggedIn = False
    
    while not isLoggedIn:
        line()
        text_centered("Sebelum masuk, harap login terlebih dahulu.")
        line()
        text_left("Menu: ")
        text_left("1. Login")
        text_left("2. Buat Akun")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            isLoggedIn = login_user()
        elif choice == "2":
            isLoggedIn = signup_user()
        else:
            text_left("Opsi tidak valid. Silakan coba lagi.")

        line()
        
    return isLoggedIn

#-----------------------------------------------------------------------------------------------------------

validasi_username = r"^[a-zA-Z0-9._]{5,}$"
Validasi_password = r"^[a-zA-Z0-9]{5,}$"

def login_user():
    while True:
        try:
            username = input("Masukkan nama pengguna: ")
            if not re.match(validasi_username, username):
                raise ValueError("Username hanya boleh berisi huruf, angka, titik, dan garis bawah dengan minimal 5 karakter.")
            else:
                break
        except ValueError as error:
            print(error)
            
    while True:
        try:
            password = input("Masukkan password: ")
            if not re.match(Validasi_password, password):
                raise ValueError("Password hanya boleh berisi huruf dan angka dengan minimal 5 karakter.")
            else:
                break
        except ValueError as error:
            print(error)

    check_user(username, password)
    if check_user(username, password) == True:
            return True
 
def signup_user():

    while True:
        try:
            username = input("Masukkan nama pengguna baru: ")
            if not re.match(validasi_username, username):
                raise ValueError("Username hanya boleh berisi huruf, angka, titik, dan garis bawah dengan minimal 5 karakter.")
            else:
                break

        except ValueError as error:
            print(error)
    
    while True:
        try:
            password = input("Masukkan password: ")
            if not re.match(Validasi_password, password):
                raise ValueError("Password hanya boleh berisi huruf dan angka dengan minimal 5 karakter.")
            else:
                break
            
        except ValueError as error:
            print(error)

    result = create_user(username, password)
    if result == True:
        return True