import database.config as config
import health.health as health
import play.category.riddle.level as riddle_level
import reward.reward as reward
import ui_utils as ui
import play.category.sequence.sequence as sequence_level


def progres_level(kategori):
    health.reset_life()
    nyawa = health.get_lives()

    print(f"\nKategori: {kategori}")
    print("Soal terdiri dari level 1-20. Jika jawaban salah, nyawa berkurang 1.")
    print("Dan jika nyawa habis, kamu harus mengulang dari level 1.")
    print(f"Total nyawa: {nyawa}\n")

    while True:
        global current_level
        if kategori == "Teka Teki Gambar":
            current_level = config.current_riddle_level
            if current_level <= 20:
                level = riddle_level.generate_question(current_level + 1)
                jawaban = level
            else :
                print("🎉Selamat! Kamu telah menyelesaikan semua level di kategori teka-teki gambar.🎉\n")
        elif kategori == "Aritmatika Dasar":
            current_level = config.current_arithmetic_level
            while current_level <= 20:
                pass
        else:
            current_level = config.current_sequence_level
            if current_level <= 20:
                level = sequence_level.show_question(current_level + 1)
                jawaban = level[0]
      
        jawaban_user = input("\nJawaban Anda: ")

        if jawaban_user.strip() == str(jawaban):
            print("Benar! Next ke level berikutnya.\n")
            reward.proses_level(kategori, current_level + 1, current_level + 1)
            current_level += 1
            if kategori == "Teka Teki Gambar":
                config.current_riddle_level = current_level
            elif kategori == "Aritmatika Dasar":
                config.current_arithmetic_level = current_level
            else :
                solusi = level[1]
                print(f"Solusi: {solusi}\n")
                config.current_sequence_level = current_level
            lanjut = input("Lanjut ke level berikutnya? (y/n): ")
            if lanjut.lower() != 'y':
                break
        else:
            repeat = health.lose_life()
            if repeat == True:
                current_level = 0
                reward.proses_level(kategori, current_level, current_level)
                