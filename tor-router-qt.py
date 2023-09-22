from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 100)

        self.button = QPushButton("Enable Tor-Router", self)
        self.button.setGeometry(80, 10, 160, 30)
        self.button.clicked.connect(on_button_click)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 75, 75)
        self.image_label.setPixmap(QPixmap("/home/user/.icons/tor-router.svg"))

        self.text_label = QLabel("hi", self)
        self.text_label.setGeometry(100, 50, 10, 10)
        self.text_label.setAlignment(Qt.AlignCenter)

        self.text_label.setStyleSheet("color: green")


def on_button_click(self):
    current_colour = self.text_label.setStyleSheet()
    new_color = "red" if current_colour == "color: green" else "green"
    self.text_label.setStyleSheet(f"color: {new_color}")


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
