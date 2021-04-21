from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QSizePolicy
from PyQt5 import QtCore


class album_button(QPushButton):
    def __init__(self, album_name):
        super(album_button, self).__init__()
        self.setObjectName(album_name)
        self.setFixedWidth(320)
        self.setMinimumHeight(32)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        self.setStyleSheet(u"QPushButton{\n"
                                      "	background-color: rgb(131, 130, 149);\n"
                                        " color: white;"
                                      "	border-radius: 4px;\n"
                                      "	border: 0px;\n"
                                      "	border-style:outset;\n"
                                      "	color: white;\n"
                                      "	set\n"
                                      "}\n"
                            )

        self.pLayout = QHBoxLayout()
        self.pTextLabel = QLabel()
        self.pTextLabel.setStyleSheet(u"QLabel{border-radius:10px;color:rbg(255,255,255);background-color: rgb(131, 130, 149);}")

        self.pTextLabel.setText(album_name);
        self.pTextLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.pTextLabel.setWordWrap(True)
        self.pTextLabel.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.pTextLabel.setMouseTracking(False)
        self.pTextLabel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        self.pLayout.addWidget(self.pTextLabel)
        self.pLayout.setAlignment(QtCore.Qt.AlignVCenter)
        self.pLayout.setSpacing(0)
        self.pLayout.setContentsMargins(0,0,0,0)

        self.setText("")
        self.setLayout(self.pLayout)
