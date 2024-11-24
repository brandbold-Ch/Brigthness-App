from PySide6.QtWidgets import QMainWindow, QApplication, QSlider
from PySide6.QtCore import Qt
from subprocess import run
import sys

class Brightness(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 50)
        self.setWindowTitle("Brightness")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setFixedSize(250, 50)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.move(0, 0)
        self.slider.setObjectName("QSlider")
        self.get_system_brightness()

        self.slider.valueChanged.connect(lambda: self.change_brightness())

    def change_brightness(self) -> None:
        try:
            run(f"xrandr --output eDP-1 --brightness {self.slider.value() / 10}", shell=True)
        except:
            ...


    def get_system_brightness(self) -> None:
        try:
            brightness = run("xrandr --verbose", shell=True, text=True, capture_output=True)
            for arg in brightness.stdout.split("\n"):
                parsed = arg.strip().split(":")

                if parsed[0] == "Brightness":
                    self.slider.setValue(int(float(parsed[1]) * 10))
        except:
            ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Brightness()
    window.show()
    sys.exit(app.exec())
