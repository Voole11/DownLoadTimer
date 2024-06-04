import os
import time

from PySide6.QtWidgets import QMessageBox
from threading import Thread
from data_vor import thieve

if os.path.exists('saved_folders'):
    with open('saved_folders', 'r') as f:
        steam_folders = f.read().split('\n')
        steam_folders = [folder for folder in steam_folders if folder != '']
else:
    steam_folders = []

def add_steam_folder(directory):
    msg = QMessageBox()
    
    folder_name = directory.split('/')[-1]
    
    if directory in steam_folders:
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Папка уже добавлена")
        msg.setWindowTitle("Error")
        msg.exec_()
        
    elif folder_name == 'downloading':
        steam_folders.append(directory)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Папка добавлена")
        msg.setWindowTitle("Success")
        msg.exec_()
        
    elif folder_name == 'steamapps':
        directory += '/downloading'
        add_steam_folder(directory= directory)
        
    else:
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Выберите папку downloadiong")
        msg.setWindowTitle("Error")
        msg.exec_()
        
    with open('saved_folders', '+w') as f:
        f.write('\n'.join(steam_folders))

def handle_time_change(Sec):
    global timeSec
    timeSec = Sec # Время, после которого вырубится комп, когда игра скачается

def shutdown(secs):
    os.system(f"shutdown -s -t {secs}")

def cancel():
    print("Отмена выключения...")
    os.system('shutdown /a')

def checker():
    if agreement_status:
        thieve(steam_folders=steam_folders)
    canceled = False
    downloading = {}
    while not canceled:
        if steam_folders != []:
            for path in steam_folders:
                if len(os.listdir(path)) != 0:
                    downloading[path] = True
            print(all(downloading.values()))
            if all(downloading.values()):
                try:
                    print(f"Загрузка завершена. Выключение через {timeSec} секунд.")
                    shutdown(timeSec)
                except:
                    print("Загрузка завершена. Выключение через 600 секунд.")
                    shutdown(600)
                canceled = True
                break
            else: 
                print("Загрузка продолжается...")
                time.sleep(30) 
                        
def start_check():
    checker_thread = Thread(target=checker)
    checker_thread.start()
    
def pass_agreement_status(status):
    global agreement_status
    agreement_status = status
