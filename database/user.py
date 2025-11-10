import json
import os

import bcrypt

import database.config as config
from database.getjson import JSON as JSON_PATH
from database.getjson import get_json
from ui_utils import error, success


def check_user(username, password):
    data = get_json()

    if username in data:
        stored_hashed = data[username].get("password")
        if stored_hashed and bcrypt.checkpw(password.encode('utf-8'), stored_hashed.encode('utf-8')):
            config.player_name = username
            config.current_level = data[username].get("total_level", 0)
            success("Login berhasil!")
            return True
        else:
            error("Password salah!")
            return False
    else:
        error("Pengguna tidak ditemukan!")
        return False

def create_user(username, password):
    data = get_json()

    if username not in data:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        data[username] = {
            "username": username,
            "password": hashed_password.decode('utf-8'),
            "total_level": 0,
            "current_riddle_level": 0,
            "current_riddle_lives": 0,
            "current_arithmetic_level": 0,
            "current_arithmetic_lives": 0,
            "current_sequence_level": 0,
            "current_sequence_lives": 0  ,
            "title": ""
        }
        with open(JSON_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    else:
        error("Pengguna sudah ada!")
        return False
        
def update_user(username, level, title):
    data = get_json()

    if username in data:
        user = data[username]
        user["total_level"] = level
        user["title"] = title
        data[username] = user
        with open(JSON_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    else:
        error("Pengguna tidak ditemukan!")
        return False
    
def logout():
    config.player_name = ""