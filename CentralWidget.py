from PyQt6.QtWidgets import QWidget, QGridLayout, QTextEdit, QLabel, QSlider, QPushButton, QSpinBox, QCheckBox, \
    QRadioButton, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import random
import string


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

#Setting Font
        font1 = QFont()
        font1.setPointSize(20)

        font2 = QFont()
        font2.setPointSize(15)

#Implementing Layout
        layout = QGridLayout(self)

#Implementing Textedit
        self.txte = QTextEdit()

        layout.addWidget(self.txte, 1,1)

        self.txte.setMaximumSize(900,20)
#Implementing Buttons
        self.btn1 = QPushButton("Copy")
        self.btn2 = QPushButton("Generate")

        layout.addWidget(self.btn1, 1,2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.btn2, 1,3, Qt.AlignmentFlag.AlignRight)

#Implementing Labels
        self.lbl1 = QLabel("Passwort anpassen: ")
        self.lbl2 = QLabel("Passwortlänge")

        layout.addWidget(self.lbl1, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.lbl2, 3, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        self.lbl1.setFont(font1)
        self.lbl2.setFont(font2)

#Implementnig Spinbox
        self.spinbox = QSpinBox()

        layout.addWidget(self.spinbox, 4,1, alignment=Qt.AlignmentFlag.AlignLeft)

        self.spinbox.setMaximumSize(37,20)

        self.spinbox.setRange(5, 30)

#Implementing Slider
        self.slider = QSlider()

        layout.addWidget(self.slider, 4,2, alignment=Qt.AlignmentFlag.AlignLeft)

        self.slider.setRange(5, 30)

#Connecting Spinbox with Slider
        self.slider.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.slider.setValue)

#Implementing Radiobuttons
        self.rdb1 = QRadioButton("Einfach auszusprechen")
        self.rdb2 = QRadioButton("Einfach zu lesen")
        self.rdb3 = QRadioButton("Alle Zeichen")

        layout.addWidget(self.rdb1, 4,3, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.rdb2, 5,3, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.rdb3, 6,3, alignment=Qt.AlignmentFlag.AlignTop)

#Implementing Checkboxes
        self.chbx1 = QCheckBox("Großbuchstaben")
        self.chbx2 = QCheckBox("Kleinbuchstaben")
        self.chbx3 = QCheckBox("Ziffern")
        self.chbx4 = QCheckBox("Sonderzeichen")

        layout.addWidget(self.chbx1, 4,4, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.chbx2, 5,4, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.chbx3, 6,4, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.chbx4, 7,4, alignment=Qt.AlignmentFlag.AlignTop)

# Implementing Slot connections
        self.btn2.clicked.connect(self.on_generate_clicked)
        self.btn1.clicked.connect(self.on_copy_clicked)

        self.setLayout(layout)

#Function Password Generator
    def generate_password(self):
        length = self.spinbox.value()
        characters = ""

        if self.chbx1.isChecked():
            characters += string.ascii_uppercase
        if self.chbx2.isChecked():
            characters += string.ascii_lowercase
        if self.chbx3.isChecked():
            characters += string.digits
        if self.chbx4.isChecked():
            characters += string.punctuation

        if not characters:
            return "Bitte Optionen auswählen"

        return ''.join(random.choice(characters) for i in range(length))

#Function´s Generate and Copy
    def on_generate_clicked(self):
        password = self.generate_password()
        self.txte.setText(password)

    def on_copy_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.txte.toPlainText())

