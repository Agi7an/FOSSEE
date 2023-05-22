from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QTextEdit,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6 import uic
import random

"""
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
"""

paths = ["Assets\Images\Fox.jpeg", "Assets\Images\AylanLogo2.png"]


class ImageWidget(QWidget):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.showImage()

    def showImage(self):
        self.image = QPixmap(self.path)
        self.image = self.image.scaled(QSize(150, 150))
        self.label = QLabel(self)
        self.label.setPixmap(self.image)
        # self.label.move(100, 100)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setMouseTracking(True)

        self.setFixedSize(QSize(800, 700))
        self.setWindowTitle("FOSSEE")
        self.mainLayout = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        # layout2.setContentsMargins(20, 20, 20, 20)
        # layout2.setSpacing(20)

        self.button1 = QPushButton("Generate", self)
        self.button1.setFixedSize(QSize(80, 50))
        self.button2 = QPushButton("Group", self)
        self.button2.setFixedSize(QSize(80, 50))

        self.button1.clicked.connect(self.generateImage)

        self.canvasLabel = QLabel()
        self.canvas = QPixmap(800, 600)
        self.canvas.fill(QColor(0, 0, 0))
        self.canvasLabel.setPixmap(self.canvas)

        self.layout2.addWidget(self.button1)
        self.layout2.addWidget(self.button2)
        # mainLayout.addWidget(self.canvasLabel)

        self.mainLayout.addLayout(self.layout2)

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

    def generateImage(self):
        print("Downloading and displaying image...")

        r = random.randint(0, len(paths) - 1)

        imageWidget = ImageWidget(paths[r])
        imageWidget.resize(100, 100)

        self.mainLayout.addWidget(imageWidget)

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse Moved!")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # self.label.setText("Left Mouse Button Pressed")
            self.label.setPixmap(QPixmap("Assets\Images\Fox.jpeg"))
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
