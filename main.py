from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
app = QApplication([])
window = QWidget()
window.resize(500,500)
nadpus = QLabel("хто такий mspetya?")
nadpus2 = QLabel("де живе mspetya?")
b1 = QRadioButton("В Житомері")
b2 = QRadioButton("В мене вдома")
v1 = QRadioButton("мотіватор")
v2 = QRadioButton("президент")
v3 = QRadioButton("рівний пацан")
v4 = QRadioButton("все одразу")
main_line = QVBoxLayout()
main_line.addWidget(nadpus, alignment=Qt.AlignmentFlag.AlignHCenter)

main_line2 = QHBoxLayout()
main_line2.addWidget(v1, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line2.addWidget(v2, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line.addLayout(main_line2)


main_line3 = QHBoxLayout()
main_line3.addWidget(v3, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line3.addWidget(v4, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line.addLayout(main_line3)

main_line.addWidget(nadpus2, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line4 = QHBoxLayout()
main_line4.addWidget(b1, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line4.addWidget(b2, alignment=Qt.AlignmentFlag.AlignHCenter)
main_line.addLayout(main_line4)
def winner():
    msg = QMessageBox()
    msg.setText("Ви перемогли")
    msg.setWindowTitle("Перемога!!")
    msg.exec()
def winner2():
    msg = QMessageBox()
    msg.setText("Ви перемогли")
    msg.setWindowTitle("Перемога!!")
    msg.exec()
v4.clicked.connect(winner)
b2.clicked.connect(winner2)








window.setLayout(main_line)
window.show()
app.exec()