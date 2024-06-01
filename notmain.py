import os
import time

from arsenii import steam_folders

timeSec = 10000 # Время, после которого вырубится комп, когда игра скачается

def shutdown():
    os.system(f"shutdown -s -t {timeSec}")

def checker():
        
        while True:

            time.sleep(30)
            
            if steam_folders != []:
                for path in steam_folders:
                    if len(os.listdir(path)) == 0:
                        print(f"Загрузка завершена. Выключение через {timeSec} секунд.")
                        shutdown()
                        break

                    else: 
                        print("Загрузка продолжается...")
                        time.sleep(30) 