from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse Moved!")
    
    def mousePressEvent(self, e):
        self.label.setText("Mouse Pressed!")

    def mouseReleaseEvent(self, e):
        self.label.setText("Mouse Released!")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("Double Clicked!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()