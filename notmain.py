import os
import time

from arsenii import steam_folders
from threading import Thread


timeSec = () # Время, после которого вырубится комп, когда игра скачается

def shutdown():
    os.system(f"shutdown -s -t {timeSec}")

def cancel():
    print("Отмена выключения...")
    os.system('shutdown /a')

def checker():
    canceled = False
    while not canceled:
        if steam_folders != []:
            for path in steam_folders:
                if len(os.listdir(path)) == 0:
                    print(f"Загрузка завершена. Выключение через {timeSec} секунд.")
                    shutdown()
                    canceled = True
                    break
                else: 
                    print("Загрузка продолжается...")
                    time.sleep(30) 
                        
def start_check():
    checker_thread = Thread(target=checker)
    checker_thread.start()