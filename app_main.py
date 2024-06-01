from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       
    
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_window = App()
    sys.exit(app.exec())