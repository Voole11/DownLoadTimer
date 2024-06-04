import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget
from PySide6.QtCore import Qt

from threading import Thread
from tkinter import filedialog as fd

from ui_main import Ui_MainWindow
from agreement_window import AgreementWindow
from notmain import handle_time_change, start_check, cancel, add_steam_folder, pass_agreement_status

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       
    
        self.show()
        
         # Подключение сигнала timeEdit к слоту handle_time_change
        self.ui.timeEdit.timeChanged.connect(self.on_time_changed)
    
        # Подключение сигнала checkBox к слоту on_checkbox_checked
        self.ui.checkBox.stateChanged.connect(self.on_checkbox_checked)
        
        self.timeSec = 0
        self.ui.toolButton.clicked.connect(lambda: add_steam_folder(fd.askdirectory(title="Выберите папку Steam", initialdir="/")))
        
    def on_time_changed(self, time):
        # Преобразование времени в секунды
        self.timeSec = time.hour() * 3600 + time.minute() * 60 + time.second()
        handle_time_change(self.timeSec)
        
    def on_checkbox_checked(self, state):
        if self.ui.checkBox.checkState() == Qt.CheckState.Checked:
            self.ui.timeEdit.setEnabled(False)
            start_check()
        else:
            self.ui.timeEdit.setEnabled(True)
            cancel()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    agreement_window = AgreementWindow()
    if agreement_window.exec() == QDialog.Accepted:
        pass_agreement_status(True)
    else:
        pass_agreement_status(False)
    agreement_window.close()
    timer_window = App()
    t1 = Thread(target=sys.exit, args=(app.exec(),))
    t1.start()