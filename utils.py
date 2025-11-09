from pyfiglet import Figlet

from ui_utils import line, space, text_left


def main_menu():
    while True:
        line()
        space()
        text_left("Menu Utama:")
        text_left("1. Mulai Permainan ⚔️")
        text_left("2. Lihat Peringkat 🏆")
        text_left("3. Keluar Aplikasi 🚪")
        space()
        choice = input("Pilih opsi (1-3): ")
        line()
        if choice == "1":
            from play.menu import chooseCategory
            chooseCategory()
        elif choice == "2":
            # Leaderboard
            from rank.leaderboard import Show_LeaderBoard
            Show_LeaderBoard()
        elif choice == "3":
            goodbye_banner()
            break
            

def banner():
    banner = Figlet(font='slant', width=80, justify='center')
    print(banner.renderText("WELCOME TO MABER"))
    line()

def goodbye_banner():
    banner = Figlet(font='slant', width=80, justify='center')
    print(banner.renderText(f"SEE YOU AGAIN! \n"))
    line()