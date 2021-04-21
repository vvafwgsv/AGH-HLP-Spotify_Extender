from PIL.ImageQt import rgb
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget


class circular_progress(QWidget):
    def __init__(self):
        super().__init__(self)

        self.value = 0
        self.width = 150
        self.height = 150
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = rgb(100, 100, 100)
        self.max_value = 100
        self.suffix = "%"
        self.text_color = rgb(255, 255, 255)
        self.enable_shadow = True

        self.resize(self.width, self.height)

    def paint_event(self, event):
        width = self.width - self.progress_width;
        height = self.height - self.progress_height;
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        painter = QPainter()
        painter.begin()
        painter.setRenderHint(QPainter.Antialiasing)

        rect = QRect(0, 0, self.width, self.height)
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

        painter.end()

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # arc
        painter.setPen(pen)
        # pyqt specific values
        painter.drawArc(margin,  margin, width, height, -90*16, -value*116)

        pen.setColor(QColor(self.text_color))
        painter.setPen(pen)
        painter.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

