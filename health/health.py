import ui_utils as ui
import database.config as config

player_lives = 5

def reset_life():
    global player_lives
    player_lives = 4

def lose_life():
    isLose = False
    global player_lives
    if player_lives > 0:
        player_lives -= 1
        ui.error(f"Nyawa berkurang! Sisa nyawa: {player_lives + 1}")
    else:
        print("Game Over! ☠")
        ui.info("Nyawa habis, ulangi dari level 1.")
        isLose = True
        reset_life()
        
    return isLose
        

def get_lives():
    return player_lives