import database.config as config
from ui_utils import info, line, space, text_left, warning


def chooseCategory():
    
    while True:
        space()
        text_left("Pilih Kategori Soal:")
        text_left("1. Aritmatika Dasar ➗")
        text_left("2. Teka Teki Gambar 🟰")
        text_left("3. Deret Angka 📏")
        text_left("4. Kembali ke Menu Utama 🔙")
        space()

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            info("Kamu memilih kategori Aritmatika Dasar.")

        elif choice == "2":
            info("Kamu memilih kategori Teka Teki Gambar.")
            from level import level
            if config.current_riddle_level == 0:
                from tutorial.tutorial import riddle_tutorial
                if riddle_tutorial():
                    level.progres_level("Teka Teki Gambar")
            else:
                level.progres_level("Teka Teki Gambar")
            break

        elif choice == "3":
            info("Kamu memilih kategori Deret Angka.")
            from level import level
            if config.current_sequence_level == 0:
                from tutorial.tutorial import sequence_tutorial
                if sequence_tutorial():
                    level.progres_level("Deret Angka")
            else:
                level.progres_level("Deret Angka")
            break


        elif choice == "4":
            info("Kembali ke Menu Utama.")
            break
        else:
            warning("Opsi tidak valid. Silakan coba lagi.")