import sys
from app import Pomodoro
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pomodoro = Pomodoro()
    sys.exit(app.exec_())