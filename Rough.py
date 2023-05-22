from PyQt6.QtCore import Qt, QSize, QMimeData, QPoint, QByteArray, QRect
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
from PyQt6.QtGui import QPixmap, QPalette, QColor, QDrag

import random
import requests
import os

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


class ImageLabel(QLabel):
    def __init__(self, parent, pixmap):
        super().__init__(parent)
        self.pixmap = pixmap

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Image Dragged")
            self.dragStartPosition = event.pos()
        elif event.button() == Qt.MouseButton.RightButton:
            print("Image Selected")

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            pixmap = self.pixmap
            mimeData.setImageData(pixmap)
            drag.setHotSpot(self.dragStartPosition - self.rect().topLeft())
            drag.setMimeData(mimeData)
            drag.exec()
            self.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.images = []
        self.setAcceptDrops(True)

        self.setFixedSize(QSize(800, 700))
        self.setWindowTitle("FOSSEE")
        self.mainLayout = QVBoxLayout()
        self.layout1 = QGridLayout()
        self.layout2 = QHBoxLayout()
        # layout2.setContentsMargins(20, 20, 20, 20)
        # layout2.setSpacing(20)

        self.button1 = QPushButton("Generate", self)
        # self.button1.setFixedSize(QSize(80, 50))
        self.button1.resize(80, 50)
        # self.button1.move(750, 650)
        self.button2 = QPushButton("Group", self)
        # self.button2.setFixedSize(QSize(80, 50))
        self.button2.resize(80, 50)
        # self.button2.move(750, 650)

        self.button1.clicked.connect(self.generateImage)

        self.layout2.addWidget(self.button1)
        self.layout2.addWidget(self.button2)

        self.layout1.setGeometry(QRect(0, 0, 700, 750))
        self.layout2.setGeometry(QRect(0, 750, 700, 50))

        # self.mainLayout.addWidget(self.canvasLabel)
        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.layout2)

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

    def generateImage(self):
        print("Downloading and displaying image...")
        downloadImage()

        path = "Assets\Images\\" + str(count) + ".svg"
        pixmap = QPixmap(path)
        label = ImageLabel(self, pixmap)
        label.setPixmap(pixmap)
        label.setGeometry(50, 50, 100, 100)

        self.layout1.addWidget(label)

        self.images.append(label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            mimeData = event.mimeData()
            imageData = mimeData.imageData()
            newLabel = ImageLabel(self, imageData)
            newLabel.setPixmap(imageData)
            newLabel.setGeometry(event.position().x(), event.position().y(), 100, 100)
            newLabel.show()

            event.accept()
        else:
            event.ignore()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
