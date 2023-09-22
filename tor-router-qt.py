#!/usr/bin/env python3
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from os import system


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 100)

        # Enable Tor-Router button
        self.button = QPushButton("Enable Tor-Router", self)
        self.button.setGeometry(80, 10, 160, 30)
        self.button.clicked.connect(on_button_click)

        # Image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 75, 75)
        self.image_label.setPixmap(QPixmap("tor-router.svg"))

        # "Tor-Router is disabled" Text
        if system("test `systemctl is-active tor-router` = 'enabled'"):
            self.text_label = QLabel("Tor-Router is disabled", self)
        else:
            self.text_label = QLabel("Tor-Router is enabled", self)
        self.text_label.setGeometry(85, 50, 150, 20)
        self.text_label.setAlignment(Qt.AlignCenter)

        self.text_label.setStyleSheet("color: red")


def on_button_click(self):
    system("pkexec tor-router")
    current_colour = self.text_label.setStyleSheet()
    self.text_label.QLabel("Tor-router")
    new_color = "red" if current_colour == "color: green" else "green"
    self.text_label.setStyleSheet(f"color: {new_color}")


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
