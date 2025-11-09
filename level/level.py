import health.health as health
import reward.reward as reward
import play.category.riddle.level as riddle_level
import ui_utils as ui
import database.config as config

def progres_level(kategori):
    current_level = config.current_level
    health.reset_life()
    nyawa = health.get_lives()

    print(f"\nKategori: {kategori}")
    print("Soal terdiri dari level 1-20. Jika jawaban salah, nyawa berkurang 1.")
    print("Dan jika nyawa habis, kamu harus mengulang dari level 1.")
    print(f"Total nyawa: {nyawa}\n")

    while current_level <= 20:
        if kategori == "Teka Teki Gambar":
            level = riddle_level.generate_question(current_level + 1)
            jawaban = level
            
        if current_level == 20:
            print("🎉Selamat! Kamu telah menyelesaikan semua level di kategori ini.🎉\n")
            break

            
        jawaban_user = input("\nJawaban Anda: ")

        if jawaban_user.strip() == str(jawaban):
            print("Benar! Next ke level berikutnya.\n")
            reward.proses_level(kategori, current_level + 1, current_level + 1)
            current_level += 1
            lanjut = input("Lanjut ke level berikutnya? (y/n): ")
            if lanjut.lower() != 'y':
                break
        else:
            repeat = health.lose_life()
            if repeat == True:
                current_level = 0
                rew13
                ard.proses_level(kategori, current_level, current_level)
                