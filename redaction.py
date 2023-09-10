from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel

import random

import base

def redwind():
    window1 = QDialog()

    mainline1 = QVBoxLayout()

    pitanna = QLabel("Питання :")
    linia = QLineEdit()

    l1 = QHBoxLayout()
    l1.addWidget(pitanna)
    l1.addWidget(linia)
    mainline1.addLayout(l1)

    pitanna2 = QLabel("Правильна відповідь :")
    linia2 = QLineEdit()

    l2 = QHBoxLayout()
    l2.addWidget(pitanna2)
    l2.addWidget(linia2)
    mainline1.addLayout(l2)

    pitanna3 = QLabel("непаравильна відповідь1 :")
    linia3 = QLineEdit()

    l3 = QHBoxLayout()
    l3.addWidget(pitanna3)
    l3.addWidget(linia3)
    mainline1.addLayout(l3)

    pitanna4 = QLabel("непаравильна відповідь2 :")
    linia4 = QLineEdit()

    l4 = QHBoxLayout()
    l4.addWidget(pitanna4)
    l4.addWidget(linia4)
    mainline1.addLayout(l4)

    pitanna5 = QLabel("непаравильна відповідь3 :")
    linia5 = QLineEdit()

    l5 = QHBoxLayout()
    l5.addWidget(pitanna5)
    l5.addWidget(linia5)
    mainline1.addLayout(l5)

    redpit = QPushButton('редангувати')
    mainline1.addWidget(redpit)

    def redquest():
        base.qeust[base.currentQuest] ={
                "питання:": linia.text(),
                "правильеа відповідь": linia2.text(),
                "неправильна1": linia3.text(),
                "неправильна2": linia4.text(),
                "неправильна3": linia5.text(),
        }
        window1.close()

    redpit.clicked.connect(redquest)

    window1.setLayout(mainline1)
    window1.show()
    window1.exec()