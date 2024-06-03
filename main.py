import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from threading import Thread
from tkinter import filedialog as fd

from ui_main import Ui_MainWindow
from notmain import handle_time_change, start_check, cancel, add_steam_folder

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
class AgreementWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пользовательское соглашение")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        label = QLabel("Пользовательское соглашение")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        agreement_text = """
        Здесь находится ваше пользовательское соглашение.
        Вы можете добавить здесь любой текст, включая правила использования вашего приложения.
        """

        text_label = QLabel(agreement_text)
        text_label.setWordWrap(True)
        layout.addWidget(text_label)

        accept_button = QPushButton("Принять")
        accept_button.clicked.connect(self.accept)
        layout.addWidget(accept_button)

        reject_button = QPushButton("Отклонить")
        reject_button.clicked.connect(self.reject)
        layout.addWidget(reject_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    agreement_window = AgreementWindow()
    if agreement_window.exec_() == QDialog.Accepted:
        print("Пользователь принял соглашение")
        # Здесь можно выполнить действия, связанные с принятием соглашения
    else:
        print("Пользователь отклонил соглашение")
        # Здесь можно выполнить действия, связанные с отклонением соглашения
    agreement_window.close()
    timer_window = App()
    t1 = Thread(target=sys.exit, args=(app.exec(),))
    t1.start()