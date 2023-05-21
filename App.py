from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QTextEdit, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6 import uic

'''
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setMouseTracking(True)

        self.setFixedSize(QSize(800, 700))
        self.setWindowTitle("FOSSEE")
        mainLayout = QVBoxLayout()
        layout2 = QHBoxLayout()
        # layout2.setContentsMargins(20, 20, 20, 20)
        # layout2.setSpacing(20)

        button1 = QPushButton("Move",self)
        button1.setFixedSize(QSize(80, 50))
        button2 = QPushButton("Group", self)
        button2.setFixedSize(QSize(80, 50))

        self.canvasLabel = QLabel()
        canvas = QPixmap(800, 600)
        canvas.fill(QColor(0, 0, 0))
        self.canvasLabel.setPixmap(canvas)

        # layout2.addWidget(Color('red'))
        layout2.addWidget(button1)
        #layout2.addWidget(Color('green'))
        layout2.addWidget(button2)
        mainLayout.addWidget(self.canvasLabel)
        mainLayout.addLayout(layout2)

        widget = QWidget()
        widget.setLayout(mainLayout)
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