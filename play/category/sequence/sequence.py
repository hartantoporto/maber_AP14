from ui_utils import line, space, text_centered, info, success, EMOJI, emoji

def generate_question(level):
    questions = {
        1: {"q": "2, 4, 6, 8, … berapa angka selanjutnya?",
            "a": 10,
            "solusi": "Alternatif Penyelesaian: 8 -> 10 (setiap angka bertambah 2)."},
        2: {"q": "Alternatif Penyelesaian: 3, 6, 9, 12, … berapa angka selanjutnya?",
            "a": 15,
            "solusi": "Pola +3: 12 -> 15."},
        3: {"q": "5, 10, 15, 20, … berapa angka ke-6?",
            "a": 30,
            "solusi": "Alternatif Penyelesaian: Setiap kali tambah 5: 25 -> 30."},
        4: {"q": "1, 2, 4, 8, 16, … berapa angka ke-7?",
            "a": 64,
            "solusi": "Pola dikali 2: 32 -> 64."},
        5: {"q": "10, 8, 3, 1, -4,... berapa angka selanjutnya?",
            "a": -6,
            "solusi": "Alternatif Penyelesaian: Selisih bergantian: -4 -> -6."},
        6: {"q": "2, 4, a, 8, 10, ... berapa nilai a?",
            "a": 6,
            "solusi": "Alternatif Penyelesaian: Pola naik 2 tiap langkah: 4 -> 6 -> 8 -> 10."},
        7: {"q": "3, 6, 9, b, 15,... berapa nilai b?",
            "a": 12,
            "solusi": "Alternatif Penyelesaian: Pola naik 3: 9 -> 12 -> 15."},
        8: {"q": "5, 10, c, 20, 25, ... berapa nilai c?",
            "a": 15,
            "solusi": "Alternatif Penyelesaian: Pola tambah 5: 10 -> 15 -> 20 -> 25."},
        9: {"q": "4, 1, 2, -3, -6, -13 ... berapa angka selanjutnya?",
            "a": -18,
            "solusi": "Alternatif Penyelesaian: Selisih: -13 -> -18."},
       10: {"q": f'Bola ajaib menggandakan dirinya setiap menit.\n1 menit = 2{emoji("ball")}, 2 menit = 4{emoji("ball")}, 3 menit = 8{emoji("ball")}, 4 menit = 16{emoji("ball")}, 5 menit = 32{emoji("ball")}.\nBerapa {emoji("ball")} di menit ke-6?',
             "a": 64,
             "solusi": "Alternatif Penyelesaian: 32 -> 64 (setiap menit ×2)."},
       11: {"q": f'1, 2, 6, 24, 120, {emoji("star")}..., berapa nilai {emoji("star")}?', 
             "a": 720,
             "solusi": "Alternatif Penyelesaian: 120 -> 720 (faktorial 6!)."},
       12: {"q": f'1, 4, 9, 16, 25, {emoji("sun")}..., berapa nilai {emoji("sun")}?', 
             "a": 36,
             "solusi": "Alternatif Penyelesaian: 25 -> 36 (kuadrat 6²)."},
       13: {"q": f'1, 1, 2, 3, 5, 8, {emoji("moon")}..., berapa nilai {emoji("moon")}?', 
             "a": 13,
             "solusi": "Alternatif Penyelesaian: 8 -> 13 (Fibonacci)."},
       14: {"q": f'3, 6, 5, 10, 7, 14, 9, {emoji("cat")}..., berapa nilai {emoji("cat")}?', 
             "a": 18,
             "solusi": "Alternatif Penyelesaian: 9 -> 18 (pola ×2 lalu -1)."},
       15: {"q": f'2, 4, 8, 10, 20, 22, {emoji("panda")}..., berapa nilai {emoji("panda")}?', 
             "a": 44,
             "solusi": "Alternatif Penyelesaian: 22 -> 44 (pola ×2)."},
       16: {"q": f'1, 4, 2, 9, 3, 16, 4, {emoji("monkey")}..., berapa nilai {emoji("monkey")}?', 
             "a": 25,
             "solusi": "Alternatif Penyelesaian: 4 -> 25 (pasangan (4,25))."},
       17: {"q": "Sintara meminjam 2 buku lebih banyak setiap hari.\nHari 1:2, Hari 2:4, Hari 3:6 ... Berapa total buku selama 5 hari?",
             "a": 30,
             "solusi": "Alternatif Penyelesaian: 2 -> 4 -> 6 -> 8 -> 10 = 30."},
       18: {"q": "Setiap hari, Sintara menjual 2× lebih banyak roti lalu +1 bonus. Hari ke-1:2 roti. Berapa di hari ke-4?",
             "a": 23,
             "solusi": "Alternatif Penyelesaian: 2 -> 5 -> 11 -> 23."},
       19: {"q": "Toko beli kain 2,6,10,14,18 m. Baju jadi 5,8,13,16,21. Jika tren konstan, berapa baju hari ke-6?",
             "a": 24,
             "solusi": "Alternatif Penyelesaian: 21 -> 24."},
       20: {"q": f"Atlet lari 2,4,12,14,42,44 km selama 6 hari. Pola berulang, berapa jarak hari ke-7?",
             "a": 132,
             "solusi": "Alternatif Penyelesaian: 44 -> 132 (pola ×3 lalu +2)."}
    }
    return questions.get(level, {"q": "Soal belum tersedia", "a": None, "solusi": "Tidak ada solusi."})

def show_question(level):
    q_data = generate_question(level)
    soal = q_data["q"]
    jawaban = q_data["a"]
    solusi = q_data["solusi"]

    for key, value in EMOJI.items():
        placeholder = f"{{{key}}}"
        if placeholder in soal:
            soal = soal.replace(placeholder, value)

    line()
    text_centered(f"Soal Level {level}")
    line()
    space()
    print(soal)
    space()
    line()
    return [jawaban, solusi]