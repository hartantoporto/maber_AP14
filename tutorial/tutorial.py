import random
import sys
import time


def typeplay(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.04))
    time.sleep(0.15)

def arithmetic_tutorial():
    print("\n==========================================")
    typeplay("   🎓 TUTORIAL MASTER ARITMATIKA 🎓\n")
    print("==========================================\n")
    typeplay("Misi Anda adalah menaklukkan berbagai tantangan numerik.\n")
    typeplay("Dari hitungan dasar hingga teka-teki cerita yang menjebak.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 1: HUKUM MATEMATIKA (KABATAKU) ===\n")
    typeplay("Di sini, urutan itu SANGAT PENTING. Ingat aturan 'KABATAKU':\n")
    typeplay("1. KAli dan BAgi dikerjakan LEBIH DULU dari TAmbah dan KUrang.\n")
    typeplay("2. TAPI! Jika ada tanda kurung ( ), mereka adalah VIP. Kerjakan duluan!\n\n")
    typeplay("Contoh:\n")
    typeplay("   4 + 3 x 2 = ?\n")
    typeplay("   JANGAN jawab 14! Yang benar adalah 4 + 6 = 10. (di sini KALI di kerjakan terlebih dahulu)\n")
    typeplay("Contoh VIP:\n")
    typeplay("   (4 + 3) x 2 = 7 x 2 = 14. (Kurung menang!)\n\n")
    typeplay("Tips Pro: Jika levelnya setara (misal KALI dan BAGI), kerjakan dari KIRI ke KANAN.\n")
    typeplay("   36 / 2 x 3 = 18 x 3 = 54.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 2: HURUF MISTERIUS (VARIABEL) ===\n")
    typeplay("Terkadang angka menyamar menjadi huruf (x, y, a, b).\n")
    typeplay("Tugasmu adalah membuka samarannya atau menemukannya.\n\n")
    typeplay("Tipe 1: Substitusi (Ganti Nilai)\n")
    typeplay("   Jika diketahui x = 3. Berapa nilai 2x + 1?\n")
    typeplay("   Artinya: 2 dikali (3) ditambah 1 = 6 + 1 = 7.\n")
    typeplay("Tipe 2: Mencari 'x'\n")
    typeplay("   x + 5 = 12\n")
    typeplay("   Agar 'x' sendirian, pindahkan +5 ke seberang menjadi -5.\n")
    typeplay("   x = 12 - 5, maka x = 7.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 3: SOAL CERITA ===\n")
    typeplay("Musuh terakhir adalah soal cerita. Senjatamu adalah LOGIKA.\n")
    typeplay("Untuk menjawab soal cerita Baca, Pahami dan Terjemahkan ke bahasa matematika.\n")
    typeplay("Contoh:\n")
    typeplay("   'Harga 2 pulpen adalah Rp6.000'\n")
    typeplay("   Terjemahan: 2 x P = 6000. Berarti 1 pulpen (P) = 3000.\n\n")
    input("[Tekan Enter untuk bersiap...]")

    print("\n==========================================")
    typeplay("           TUTORIAL SELESAI\n")
    print("==========================================\n")
    while True:
        lanjut_ulang_arithmetic = input("Tekan [Enter] untuk memulai! Ketik [Ulang] untuk melihat ulang tutorial: ")
        if lanjut_ulang_arithmetic == "":
            break
        elif lanjut_ulang_arithmetic.lower() == "ulang":
            arithmetic_tutorial()
        else:
            print("Input tidak dikenal! Silahkan hanya tekan Enter atau ketik 'Ulang'.")

def riddle_tutorial():
    print("\n==========================================")
    typeplay("   🎓 TUTORIAL MASTER TEKA-TEKI MATEMATIKA 🎓\n")
    print("==========================================\n")
    typeplay("Misi Anda adalah memecahkan nilai dibalik simbol-simbol misterius.\n")
    typeplay("Setiap bentuk (◼, ▲, ●, ◆, ○) mewakili sebuah ANGKA yang unik.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 1: DASAR ===\n")
    typeplay("Anda harus menemukan nilai simbol dari PETUNJUK yang diberikan.\n")
    typeplay("Contoh Petunjuk 1:\n")
    typeplay("   ◼ + ◼ = 10\n")
    typeplay("Artinya: Dua buah ◼ jika dijumlahkan hasilnya 10.\n")
    typeplay("Maka, nilai satu ◼ adalah 5.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 2: PETUNJUK LANJUT ===\n")
    typeplay("Di level yang lebih tinggi, petunjuk mungkin terlihat seperti ini:\n")
    typeplay("   ▲ * ▲ * ▲ = 27\n")
    typeplay("Jangan panik! Ini artinya sebuah angka dikalikan dengan dirinya sendiri 3 kali hasilnya 27.\n")
    typeplay("3 x 3 x 3 = 27.\n")
    typeplay("Jadi, nilai ▲ adalah 3.\n")
    typeplay("Petunjuk lain:\n")
    typeplay("   ● + ● + ● = 15  -> Artinya 3 x ● = 15, jadi ● = 5.\n\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 3: MENYELESAIKAN MISI ===\n")
    typeplay("Setelah menemukan nilai semua simbol, selesaikan soal utamanya.\n")
    typeplay("Jika kita tahu:\n")
    typeplay("   ◼ = 5")
    typeplay("   ▲ = 3")
    typeplay("\nMaka Pertanyaan:\n")
    typeplay("   ◼ + ▲ = ?\n")
    typeplay("\nJawabannya adalah 8 (karena 5 + 3 = 8).\n\n")
    input("[Tekan Enter untuk bersiap...]")

    print("\n==========================================")
    typeplay("           TUTORIAL SELESAI\n")
    print("==========================================\n")
    while True:
        lanjut_ulang_riddle = input("Tekan [Enter] untuk memulai! Ketik [Ulang] untuk melihat ulang tutorial: ")
        if lanjut_ulang_riddle == "":
            return True
        elif lanjut_ulang_riddle.lower() == "ulang":
            riddle_tutorial()
        else:
            print("Input tidak dikenal! Silahkan hanya tekan Enter atau ketik 'Ulang'.")

def sequence_tutorial():
    print("\n==========================================")
    typeplay("   🎓 TUTORIAL MASTER BARIS DERET ANGKA 🎓\n")
    print("==========================================\n")
    typeplay("Misi Anda: Menemukan angka yang hilang berdasarkan POLA tersembunyi.\n")
    typeplay("Ada 4 Kunci yang harus dikuasai untuk menaklukkan semua soal.\n\n")
    input("[Tekan Enter untuk mempelajari Bagian 1...]")

    typeplay("\n=== BAGIAN 1: POLA DASAR (TETAP) ===\n")
    typeplay("Cek selisih antar angka. Apakah selalu sama?\n")
    typeplay("🔹 Aritmatika (Tambah/Kurang):\n")
    typeplay("   Contoh: 2, 4, 6, 8... (Selalu +2)\n")
    typeplay("   -> Angka berikutnya: 8 + 2 = 10\n")
    typeplay("🔹 Geometri (Kali/Bagi):\n")
    typeplay("   Contoh: 3, 6, 12, 24... (Selalu dikali 2)\n")
    typeplay("   -> Angka berikutnya: 24 x 2 = 48\n")
    typeplay("Tips: Level 1-8 dan 10 menggunakan pola ini!\n\n")
    input("[Tekan Enter untuk lanjut ke Bagian 2...]")

    typeplay("\n=== BAGIAN 2: POLA BILANGAN KHUSUS ===\n")
    typeplay("Kadang polanya bukan tambah/kali biasa, tapi pola unik:\n")
    typeplay("⭐ Pola Kuadrat (Pangkat 2):\n")
    typeplay("   1, 4, 9, 16... -> Ini adalah 1², 2², 3², 4².\n")
    typeplay("   Selanjutnya 5² = 25.\n")
    typeplay("🌛 Pola Fibonacci (Jumlah 2 angka sebelumnya):\n")
    typeplay("   1, 1, 2, 3, 5... -> (1+1=2), (1+2=3), (2+3=5).\n")
    typeplay("   Selanjutnya 3+5 = 8.\n")
    typeplay("❗ Pola Faktorial (Pengali makin besar):\n")
    typeplay("   1, 2, 6, 24... -> (x2, x3, x4).\n")
    typeplay("   Selanjutnya dikali 5 -> 24 x 5 = 120.\n\n")
    input("[Tekan Enter untuk lanjut ke Bagian 3...]")

    typeplay("\n=== BAGIAN 3: POLA KOMBINASI (SELANG-SELING) ===\n")
    typeplay("Level tinggi sering menjebak! Jika pola biasa tidak ketemu, coba ini:\n")
    typeplay("🅰️ Dua Operasi Bergantian:\n")
    typeplay("   Contoh: 2, 4, 5, 10, 11...\n")
    typeplay("   Polanya: (x2), (+1), (x2), (+1)...\n")
    typeplay("🅱️ Pola Lompat (Ganjil & Genap beda jalur):\n")
    typeplay("   Contoh: 1, 9, 2, 16, 3, 25...\n")
    typeplay("   Posisi Ganjil: 1, 2, 3... (Maju +1)\n")
    typeplay("   Posisi Genap: 9, 16, 25... (Bilangan kuadrat)\n")
    input("[Tekan Enter untuk lanjut...]")

    typeplay("\n=== BAGIAN 4: MEMBACA SOAL CERITA 📖 ===\n")
    typeplay("Jangan panik dengan teks panjang. Ubah cerita menjadi deret angka!\n")
    typeplay("Contoh: 'Setiap hari Budi meminjam 2 buku lebih banyak...'\n")
    typeplay("-> Artinya: +2 setiap hari (Deret Aritmatika: 2, 4, 6...).\n")
    input("[Tekan Enter untuk bersiap...]")

    print("\n==========================================")
    typeplay("           TUTORIAL SELESAI\n")
    print("==========================================\n")
    while True:
        lanjut_ulang_sequence = input("Tekan [Enter] untuk memulai! Ketik [Ulang] untuk melihat ulang tutorial: ")
        if lanjut_ulang_sequence == "":
            return True
        elif lanjut_ulang_sequence.lower() == "ulang":
            sequence_tutorial()
        else:
            print("Input tidak dikenal! Silahkan hanya tekan Enter atau ketik 'Ulang'.")
