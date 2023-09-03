from PyQt5.QtWidgets import *

import base


def meniuwind():
    window = QDialog()

    mainline = QVBoxLayout()

    questbl = QLabel("Питання :")
    questEdit = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(questbl)
    h1.addWidget(questEdit)
    mainline.addLayout(h1)

    truans = QLabel("Правильна відповідь :")
    questEdit2 = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget(truans)
    h2.addWidget(questEdit2)
    mainline.addLayout(h2)

    falans1 = QLabel("неправильна відповідь1 :")
    questEdit3 = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget(falans1)
    h3.addWidget(questEdit3)
    mainline.addLayout(h3)

    falans2 = QLabel("неправильна відповідь2 :")
    questEdit4 = QLineEdit()

    h4 = QHBoxLayout()
    h4.addWidget(falans2)
    h4.addWidget(questEdit4)
    mainline.addLayout(h4)

    falans3 = QLabel("неправильна відповідь3 :")
    questEdit5 = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget(falans3)
    h5.addWidget(questEdit5)
    mainline.addLayout(h5)

    donebut = QPushButton('готово')
    mainline.addWidget(donebut)

    def addquest():
        base.qeust.append(
            {
                "питання:": questEdit.text(),
                "правильеа відповідь": questEdit2.text(),
                "неправильна1": questEdit3.text(),
                "неправильна2": questEdit4.text(),
                "неправильна3": questEdit5.text(),
            }
        )

        window.hide()


    donebut.clicked.connect(addquest)

    window.setLayout(mainline)
    window.show()
    window.exec()