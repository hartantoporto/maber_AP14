from tutorial.tutorial import tutorial_barisan_deret
from play.category.sequence.sequence import generate_question
from ui_utils import info, error, success, line
from database import config
from reward import reward
from database.user import get_user_info, update_user

def main_sequence():
    if not tutorial_barisan_deret():
        info("Kembali ke menu utama.")
        return

    if not hasattr(config, "player_name") or not config.player_name:
        error("Pengguna tidak ditemukan! Login dulu ya.")
        return

    player = config.player_name
    user_info = get_user_info(player)

    if not user_info.get("title"):
        user_info["title"] = "Tingkat 0 = Bronze"
    if "total_level" not in user_info:
        user_info["total_level"] = 0

    update_user(player, user_info["total_level"], user_info["title"])

    current_level = user_info["total_level"] + 1
    max_level = 20
    lives = 5

    line()
    print("Kategori: Deret Angka")
    print(f"Total nyawa: {lives}")
    print(f"Title: {user_info['title']}")
    line()

    while current_level <= max_level:
        soal = generate_question(current_level)
        print(f"\nLevel {current_level}: {soal['q']}")

        while True:
            answer = input("Jawaban Anda (angka saja): ").strip()
            try:
                answer_int = int(answer)
            except ValueError:
                error("Jawaban harus berupa angka!")
                continue

            if answer_int == soal["a"]:
                success("Benar!")
                print(soal.get("solusi", ""))

                total_level = current_level
                reward.proses_level("Deret Angka", current_level, total_level)

                title_baru = reward.cek_tingkat(total_level)
                update_user(player, total_level, title_baru)

                current_level += 1

                while True:
                    lanjut = input("Lanjut ke level berikutnya? (y/n): ").lower().strip()
                    if lanjut in ("y", "n"):
                        break
                    else:
                        error("Input tidak valid! Pilih 'y' atau 'n'.")
                if lanjut == "n":
                    info("Permainan berhenti.")
                    return
                break

            else:
                lives -= 1
                error("Salah!")
                print(f"Sisa nyawa: {lives}")

                if lives <= 0:
                    error("Nyawa habis! Ulang dari level terakhir + 1.")
                    lives = 5
                    current_level = user_info["total_level"] + 1
                    break

                while True:
                    lanjut = input("Mau coba lagi level ini? (y/n): ").lower().strip()
                    if lanjut in ("y", "n"):
                        break
                    else:
                        error("Input tidak valid! Pilih 'y' atau 'n'.")
                if lanjut == "n":
                    info("Permainan berhenti.")
                    return
                else:
                    print("Coba lagi level ini!")