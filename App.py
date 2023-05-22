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

import random
import requests
import os

"""
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
"""

names = [
    "1F4A0.svg",
    "1F518.svg",
    "1F532.svg",
    "1F533.svg",
    "1F534.svg",
    "1F535.svg",
    "1F536.svg",
    "1F537.svg",
    "1F538.svg",
    "1F539.svg",
    "1F53A.svg",
    "1F53B.svg",
    "1F7E0.svg",
    "1F7E1.svg",
    "1F7E2.svg",
    "1F7E3.svg",
    "1F7E4.svg",
    "1F7E5.svg",
    "1F7E6.svg",
    "1F7E7.svg",
    "1F7E8.svg",
    "1F7E9.svg",
    "1F7EA.svg",
    "1F7EB.svg",
    "25AA.svg",
    "25AB.svg",
    "25FB.svg",
    "25FC.svg",
    "25FD.svg",
    "25FE.svg",
    "26AA.svg",
    "26AB.svg",
    "2B1B.svg",
    "2B1C.svg",
]

count = 0


def downloadImage():
    url = (
        "https://github.com/hfg-gmuend/openmoji/raw/master/src/symbols/geometric/"
        + names[random.randint(0, len(names) - 1)]
    )

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        global count
        count += 1
        # Get the file name from the URL
        file_name = "Assets\Images\\" + str(count) + ".svg"

        # Save the image to disk
        with open(file_name, "wb") as file:
            file.write(response.content)

        print(f"Image downloaded: {file_name}")
    else:
        print("Failed to download the image.")


downloadImage()


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
        downloadImage()

        imageWidget = ImageWidget("Assets\Images\\" + str(count) + ".svg")
        imageWidget.resize(100, 100)

        self.mainLayout.addWidget(imageWidget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
