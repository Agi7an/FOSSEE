from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QWidget, QGridLayout
from PyQt6.QtGui import QPixmap, QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setMouseTracking(True)

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("FOSSEE")
        layout = QGridLayout()

        self.label = QLabel("Click in this window")

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(self.label, 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse Moved!")
    
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # self.label.setText("Left Mouse Button Pressed")
            self.label.setPixmap(QPixmap('Assets\Images\Fox.jpeg'))
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