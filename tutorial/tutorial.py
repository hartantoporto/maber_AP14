def tutorial_hitung_campuran():
    print("=" * 80)
    print("  TUTORIAL: Aritmatika Dasar")
    print("=" * 80)
    print("\nDalam operasi hitung campuran, urutan pengerjaan sangat penting.")
    print("Aturan yang harus diikuti adalah 'KuKaBaTaKu':")
    print("\n1. KURUNG ()")
    print("   - Kerjakan semua operasi di dalam tanda kurung terlebih dahulu.")
    print("   - Contoh: 10 + (5 - 2) -> Kerjakan (5 - 2) dulu jadi 3.")
    
    print("\n2. KALI (x) dan BAGI (:)")
    print("   - Setelah kurung, kerjakan perkalian dan pembagian.")
    print("   - Keduanya sama kuat, kerjakan dari yang paling kiri.")
    print("   - Contoh: 10 + 4 x 2 -> Kerjakan 4 x 2 dulu jadi 8.")
    print("   - Contoh: 12 : 2 x 3 -> Kerjakan 12 : 2 dulu jadi 6, baru 6 x 3 = 18.")

    print("\n3. TAMBAH (+) dan KURANG (-)")
    print("   - Terakhir, kerjakan pertambahan dan pengurangan.")
    print("   - Keduanya sama kuat, kerjakan dari yang paling kiri.")
    
    print("\n--- CONTOH LENGKAP ---")
    print("Soal: 5 + ( 10 - 2 ) x 3 : 4 - 1")
    print("1. Kurung: 5 + (8) x 3 : 4 - 1")
    print("2. Kali/Bagi (dari kiri):")
    print("   - Kali: 5 + 24 : 4 - 1")
    print("   - Bagi: 5 + 6 - 1")
    print("3. Tambah/Kurang (dari kiri):")
    print("   - Tambah: 11 - 1")
    print("   - Kurang: 10")
    print("\nHasil Akhir: 10")
    print("\n========================================")

def tutorial_tekateki_gambar():
    print("=" * 80)
    print("   TUTORIAL: Teka-Teki Gambar dan Operasi")
    print("=" * 80)
    print("\nJenis soal ini menantang Anda untuk menemukan nilai setiap bentuk")
    print("berdasarkan pola operasi matematika yang diberikan ( + , - , × , ÷ ).")
    print("Setiap bentuk (misalnya ◼, ▲, ●, ◆, ○) mewakili nilai angka tertentu.")
    
    print("\nCara Mengerjakan:")
    print("1. Perhatikan Bentuk dan Operasi")
    print("   - Tiap soal menggunakan simbol-simbol acak seperti ◼, ▲, ●, ◆, ○.")
    print("   - Setiap simbol punya nilai berbeda.")
    print("   - Soal ditulis seperti:  ◼ + ▲ = ?  atau  ● × ◼ ÷ ▲ = ?")

    print("\n2. Gunakan Petunjuk (Hint) untuk Menemukan Nilai Simbol")
    print("   - Tiap hint menunjukkan hubungan antar bentuk dengan hasil hitungan.")
    print("   - Contoh hint:  ◼ + ◼ + ◼ = 9  → berarti nilai ◼ = 3.")
    print("   - Gunakan semua hint yang tersedia untuk menentukan nilai setiap bentuk.")

    print("\n3. Substitusi Nilai ke Dalam Soal Utama")
    print("   - Setelah tahu nilai tiap bentuk, gantikan simbol pada soal.")
    print("   - Lakukan operasi matematika sesuai urutan (ingat urutan operasi: ×/÷ lebih dulu).")

    print("\n4. Hasilkan Jawaban Akhir")
    print("   - Hitung hasil akhir setelah semua simbol diganti nilainya.")
    print("   - Beberapa soal mungkin melibatkan operasi campuran ( + , - , × , ÷ ).")

    print("\n--- CONTOH ---")
    print("Soal:   ◼ + ▲ = ?")
    print("Petunjuk:")
    print("  ◼ + ◼ + ◼ = 9")
    print("  ▲ + ▲ + ▲ = 6")
    print("Analisis:")
    print("  Dari hint pertama → ◼ = 3")
    print("  Dari hint kedua   → ▲ = 2")
    print("Substitusi ke soal utama → 3 + 2 = 5")
    print("Jawaban: 5")

    print("\n--- CATATAN TAMBAHAN ---")
    print("• Pada level lebih tinggi, operasi bisa lebih rumit (campuran +, -, ×, ÷).")
    print("• Beberapa hint menunjukkan pola kombinasi, bukan nilai langsung.")
    print("• Fokuslah pada hubungan antar bentuk, bukan pada angka di hint saja.")
    print("• Gunakan logika dan perhatikan urutan operasi.")

    print("\nSelamat berpikir dan temukan pola tersembunyi di balik simbol-simbol tersebut!")
    print("=" * 80)
    
    continuePlay = input("Ingin memulai permainan Teka-Teki Gambar? (y): ")
    if continuePlay.lower() == 'y':
        return True
    else:
        return False


def tutorial_barisan_deret():
    if getattr(tutorial_barisan_deret, "_done", False):
        return True 
    print("=" * 80)
    print("    TUTORIAL: Matematika Barisan & Deret")
    print("=" * 80)
    
    print("\nApa itu Barisan dan Deret?")
    print("- Barisan: urutan angka dengan pola tertentu.")
    print("  Contoh mudah:")
    print("    1, 2, 3, 4, 5 -> setiap suku bertambah +1 (aritmetika)")
    print("    2, 4, 8, 16 -> setiap suku dikali 2 (geometri)")
    print("    1, 1, 2, 3, 5 -> jumlah 2 suku sebelumnya (Fibonacci)")

    print("\n- Deret: jumlah dari suku-suku barisan tersebut.")
    print("  Contoh mudah:")
    print("    Barisan: 1,2,3,4,5 -> Deret: 1+2+3+4+5 = 15")
    
    print("\nContoh soal cerita sederhana:")
    print("- Ani menaruh 1 kelereng di hari pertama, 2 di hari kedua, 3 di hari ketiga, dan seterusnya.")
    print("  Pertanyaannya: Berapa kelereng yang Ani miliki di hari ke-5?")
    print("  Tips: ubah kata menjadi angka -> 1,2,3,4,5 -> pola tambah +1 -> jawab 5 kelereng")
    
    print("- Bola ajaib yang bertambah 2 tiap menit: 2 bola, 4 bola, 6 bola,...")
    print("  Pertanyaannya: Berapa bola di menit ke-4?")
    print("  Tips: Perhatikan pola aritmetika (+2) -> jawab 8 bola")
    
    print("\nTips cepat menyelesaikan soal cerita:")
    print("- Ubah kata-kata menjadi angka dulu.")
    print("- Tentukan pola: tambah tetap (aritmetika) atau kali tetap (geometri).")
    print("- Perhatikan pola bergantian atau campuran jika ada.")
    
    print("=" * 80)
    
    start = input("Ingin memulai permainan Barisan dan Deret? (y/n): ").lower().strip()
    while start not in ('y', 'n'):
        print("Pilih 'y' atau 'n' saja!")
        start = input("Ingin memulai permainan Barisan dan Deret? (y/n): ").lower().strip()

    tutorial_barisan_deret._done = True
    return start == 'y'