import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from database.getjson import get_json

def Show_LeaderBoard():
    print("--- 🏆 Papan Peringkat 🏆 ---")

    datap_user = get_json()

    if not datap_user:
        print("Belum ada data pemain.")
        print("-----------------------------")
        return
    
    list_user = list(datap_user.values())

    leaderboard_sorted = sorted(list_user, key=lambda user: user["total_level"], reverse=True)

    for index, user in enumerate(leaderboard_sorted, start=1):
        # 'start=1' membuat 'enumerate' memulai hitungan dari 1 (untuk peringkat)
        username = user.get("username", "N/A")
        level = user.get("total_level", 0)
        title = user.get("title", "-")
        
        print(f"#{index:<3} | {username:<15} | Level: {level:<5} | Title: {title}")
    
    print("-----------------------------")
