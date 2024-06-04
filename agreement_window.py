from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QPushButton
from PyQt6.QtCore import Qt

class AgreementWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пользовательское соглашение")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        label = QLabel("Пользовательское соглашение")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        with open('eula.txt', 'r', encoding='utf-8') as file:
            agreement_text = file.read()

        text_label = QLabel(agreement_text)
        text_label.setWordWrap(True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.addWidget(text_label)
        scroll_widget.setLayout(scroll_layout)
        
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        accept_button = QPushButton("Принять")
        accept_button.clicked.connect(self.accept)
        layout.addWidget(accept_button)

        reject_button = QPushButton("Отклонить")
        reject_button.clicked.connect(self.reject)
        layout.addWidget(reject_button)

        self.setLayout(layout)