from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setMouseTracking(True)

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse Moved!")
    
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Left Mouse Button Pressed")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("Right Mouse Button Pressed")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Middle Mouse Button Pressed")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Left Mouse Button Released")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("Right Mouse Button Released")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Middle Mouse Button Released")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Left Mouse Button Double Clicked")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("Right Mouse Button Double Clicked")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Middle Mouse Button Double Clicked")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()