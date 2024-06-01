from PySide6.QtWidgets import QMessageBox

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
        
    print(steam_folders)
