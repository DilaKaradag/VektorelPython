import sys

from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İçiçe (Nested) Layout")
        disLayout = QVBoxLayout() # Dış layout
       
        ustLayout = QFormLayout() # Form Layout
        ustLayout.addRow("Veri gir: ", QLineEdit())
       
        seceneklerLayout = QVBoxLayout()
        seceneklerLayout.addWidget(QCheckBox("Seçenek 1"))
        seceneklerLayout.addWidget(QCheckBox("Seçenek 2"))
        seceneklerLayout.addWidget(QCheckBox("Seçenek 3"))
       
        # Dış layout içine yerleşim
        disLayout.addLayout(ustLayout)
        disLayout.addLayout(seceneklerLayout)
       
        self.setLayout(disLayout) # Pencere ana layout u

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()