from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Pomodoro(QWidget):

    def __init__(self, parent=None):
        super(Pomodoro, self).__init__(parent)
        self._grid = QGridLayout(self)

        self._time_label = QLabel("00:00:00")

        self._start_button = QPushButton("Start")
        self._stop_button = QPushButton("Stop")

        self._pomodoro_button = QPushButton("25 Minutes")
        self._long_break_button = QPushButton("15 Minutes")
        self._short_break_button = QPushButton("5 Minutes")

        self._stylesheet = open("style.qss", "r")

        self._configure_layout()
        self._configure_styles()
        self._configure_widgets()

    def _configure_layout(self):
        self._grid.addWidget(self._time_label, 0, 0, 1, 3)

        self._grid.addWidget(self._start_button, 1, 0, 1, 2)
        self._grid.addWidget(self._stop_button, 1, 2, 1, 1)

        self._grid.addWidget(self._pomodoro_button, 2, 0, 1, 1)
        self._grid.addWidget(self._long_break_button, 2, 1, 1, 1)
        self._grid.addWidget(self._short_break_button, 2, 2, 1, 1)
        
    def _configure_styles(self):
        self._time_label.setStyleSheet(" background-color: #fff; ")

    def _configure_widgets(self):

        #Time Label Widget
        self._time_label.setAlignment(Qt.AlignCenter)

        #Main Widget
        self.setStyleSheet(self._stylesheet.read())
        self.setWindowTitle("Pomodoro")
        self.setFixedSize(400, 200)
        self.show()

    def __del__(self):
        self._stylesheet.close()