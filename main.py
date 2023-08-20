from PyQt5.QtWidgets import *

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
answersgroup.setLayout(answerline)
mainline.addWidget(answersgroup)

ansbut = QPushButton('відповісти')
mainline.addWidget(ansbut)

window.setLayout(mainline)
window.show()
app.exec()