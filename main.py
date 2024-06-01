import os
import time

path = "C:\\Program Files (x86)\\Steam\\steamapps\\downloading"
timeSec = 10000 # Время, после которого вырубится комп, когда игра скачается

def shutdown():
    os.system(f"shutdown -s -t {timeSec}")

def checker():
        
        while True:
            
            time.sleep(30)

            if len(os.listdir(path)) == 0:
                print("Загрузка завершена. Выключение через {} секунд.".format(timeSec))
                shutdown()
                break

            else: 
                print("Загрузка продолжается...")
                time.sleep(30) 

checker()