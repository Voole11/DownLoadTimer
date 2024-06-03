from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from threading import Thread

def timer():
    time = Ui_MainWindow.time_func()
    return time 
class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       
    
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_window = App()
    t1 = Thread(target=sys.exit, args=(app.exec(),))
    t1.start()