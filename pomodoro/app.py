from PyQt5.QtWidgets import QWidget, QMenuBar, QAction, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer


class Pomodoro(QWidget):

    TICK_RATE = 1000

    SEC_IN_MIN = 60

    def __init__(self, parent=None):
        super(Pomodoro, self).__init__(parent)
        self._timer = QTimer()

        self._duration = 0
        self._time_left = 0
        self._stopped = True

        self._grid = QGridLayout(self)

        self._time_label = QLabel("00:00")

        self._start_button = QPushButton("Start")
        self._stop_button = QPushButton("Stop")

        self._pomodoro_button = QPushButton("25 Minutes")
        self._long_break_button = QPushButton("15 Minutes")
        self._short_break_button = QPushButton("5 Minutes")

        self._stylesheet = open("style.qss", "r")

        self._configure_events()
        self._configure_layout()
        self._configure_styles()
        self._configure_widgets()

    def _configure_events(self):
        self._timer.timeout.connect(self._timer_timeout)
        
        self._start_button.clicked.connect(self._start_timer)
        self._stop_button.clicked.connect(self._stop_timer)

        self._pomodoro_button.clicked.connect(self._set_timer_for_pomodoro)
        self._long_break_button.clicked.connect(self._set_timer_for_long_break)
        self._short_break_button.clicked.connect(self._set_timer_for_short_break)

    def _configure_layout(self):
        self._grid.addWidget(self._time_label, 1, 0, 1, 3)

        self._grid.addWidget(self._start_button, 2, 0, 1, 2)
        self._grid.addWidget(self._stop_button, 2, 2, 1, 1)

        self._grid.addWidget(self._pomodoro_button, 3, 0, 1, 1)
        self._grid.addWidget(self._long_break_button, 3, 1, 1, 1)
        self._grid.addWidget(self._short_break_button, 3, 2, 1, 1)
        
    def _configure_styles(self):
        self._time_label.setStyleSheet(" background-color: #fff; ")

    def _configure_widgets(self):

        #Time Label Widget
        self._time_label.setAlignment(Qt.AlignCenter)

        #Main Widget
        self.setStyleSheet(self._stylesheet.read())
        self.setWindowTitle("Pomodoro")
        self.setFixedSize(400, 250)
        self.show()


    def _timer_timeout(self):
        self._time_left -= 1

        if self._time_left <= 0:
            self._reset_timer()

        self._update_gui(self._time_left)  

    def _start_timer(self):
        self._stopped = False

        if self._duration != 0:
            self._timer.start(Pomodoro.TICK_RATE)

    def _stop_timer(self):
        if self._duration != 0:
            self._timer.stop()

        if self._stopped:
            self._reset_timer()

        self._stopped = True

    def _reset_timer(self):
        self._timer.stop()
        self._duration = 0
        self._time_left = 0
        self._update_gui(self._time_left)

    def _init_timer(self, duration):
        if self._stopped:
            self._duration = duration
            self._time_left = Pomodoro.SEC_IN_MIN * self._duration
            self._update_gui(self._time_left)

    def _set_timer_for_pomodoro(self):
        self._init_timer(25)

    def _set_timer_for_long_break(self):
        self._init_timer(15)


    def _set_timer_for_short_break(self):
        self._init_timer(5)
      
    def _update_gui(self, time):
        self._time_label.setText(self._get_formatted_time(self._time_left))

    def _get_formatted_time(self, time):
        minutes = self._get_minutes(time)
        seconds = self._get_seconds(time)

        if seconds <= 9:
            return str("{0}:0{1}".format(minutes, seconds))
        else:
            return str("{0}:{1}".format(minutes, seconds))

    def _get_minutes(self, time):
        return int(time / Pomodoro.SEC_IN_MIN)

    def _get_seconds(self, time):
        return time - (Pomodoro.SEC_IN_MIN * self._get_minutes(time))

    def __del__(self):
        self._stylesheet.close()