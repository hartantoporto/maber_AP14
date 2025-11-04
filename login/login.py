from utils import header, line, space, text_centered, text_left


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

def login_user():
    return True  
 
def signup_user():
    return True   