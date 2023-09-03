from PyQt5.QtWidgets import *
import base
import random
from meniu import meniuwind

app = QApplication([])
window = QWidget()
window.resize(400 , 300)

mainline = QVBoxLayout()

menubut = QPushButton('меню')
restbtn = QPushButton('Відпочити')
timespn = QSpinBox()
timlb = QLabel('хвилин')

firstline = QHBoxLayout()
firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timespn)
firstline.addWidget(timlb)
mainline.addLayout(firstline)

quetext = QLabel('скільки отчімів у a4 ?')
mainline.addWidget(quetext)

answersgroup = QGroupBox('варіанти відповідей')
answer1 = QRadioButton('1')
answer2 = QRadioButton('2')
answer3 = QRadioButton('3')
answer4 = QRadioButton('4')
answerline = QVBoxLayout()
answerline.addWidget(answer1)
answerline.addWidget(answer2)
answerline.addWidget(answer3)
answerline.addWidget(answer4)
answers = [answer1 , answer2 , answer3 , answer4]
answersgroup.setLayout(answerline)
mainline.addWidget(answersgroup)

result = QLabel('Результат :')
answerline.addWidget(result)
result.hide()

ansbut = QPushButton('відповісти')
nextque = QPushButton('наступне питання')
mainline.addWidget(ansbut)
mainline.addWidget(nextque)
nextque.hide()

def shovresult():
    for i in range(4):
        answers[i].hide()
    result.show()
    nextque.show()
    ansbut.hide()
    if answers[0].isChecked():
        result.setText('правильно')
    else:
        result.setText('не правильно')

def showqueshon():
    random.shuffle(answers)
    quetext.setText(base.qeust[base.currentQuest]['питання:'])
    answers[0].setText(base.qeust[base.currentQuest]['правильеа відповідь'])
    answers[1].setText(base.qeust[base.currentQuest]['неправильна1'])
    answers[2].setText(base.qeust[base.currentQuest]['неправильна2'])
    answers[3].setText(base.qeust[base.currentQuest]['неправильна3'])

def showqueshon2():
    random.shuffle(answers)
    base.currentQuest += 1
    quetext.setText(base.qeust[base.currentQuest]['питання:'])
    answers[0].setText(base.qeust[base.currentQuest]['правильеа відповідь'])
    answers[1].setText(base.qeust[base.currentQuest]['неправильна1'])
    answers[2].setText(base.qeust[base.currentQuest]['неправильна2'])
    answers[3].setText(base.qeust[base.currentQuest]['неправильна3'])
    result.hide()
    nextque.hide()
    for i in range(4):
        answers[i].show()
    ansbut.show()

showqueshon()
ansbut.clicked.connect(shovresult)
nextque.clicked.connect(showqueshon2)
menubut.clicked.connect(meniuwind)

window.setLayout(mainline)
window.show()
app.exec()