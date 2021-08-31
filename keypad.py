import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QPushButton)


global BUTTON_up
global BUTTON_down
global BUTTON_input
global BUTTON_cancel
global BUTTON_enter
global BUTTON_correction
global BUTTON_consonant
global BUTTON_number
global BUTTON_vowels


# 버튼 눌렀을때 발생하는 이밴트
def start_c():
    global BUTTON_start
    BUTTON_start = 1
    print(BUTTON_start)

def up_c(self):
    BUTTON_up = 1
    print(BUTTON_up)


def down_c(self):
    BUTTON_down = 1
    print(BUTTON_down)


def input_c(self):
    BUTTON_input = 1
    print(BUTTON_input)


def cancel_c(self):
    BUTTON_cancel = 1
    print(BUTTON_cancel)


def enter_c(self):
    BUTTON_enter = 1
    print(BUTTON_enter)


def cerrection_c(self):
    BUTTON_correction = 1
    print(BUTTON_correction)


def consonant_c(self):
    BUTTON_consonant = 1
    print(BUTTON_consonant)


def number_c(self):
    BUTTON_number = 1
    print(BUTTON_number)


def vowels_c(self):
    BUTTON_vowels = 1
    print(BUTTON_vowels)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 모양 구현
        grid = QGridLayout()
        self.setLayout(grid)
        lbl_display = QLabel('화면')
        pb_consonant = QPushButton("자음", self)
        pb_vowels = QPushButton('모음', self)
        pb_number = QPushButton('숫자', self)
        pb_start = QPushButton('시작', self)
        pb_correction = QPushButton('정정', self)
        pb_up = QPushButton('\u2191', self)
        pb_input = QPushButton('입력', self)
        pb_down = QPushButton('\u2193', self)
        pb_enter = QPushButton('확인', self)
        pb_cancel = QPushButton('취소', self)

        grid.addWidget(lbl_display, 0, 0, 3, 3)  # 화면 크기 설정
        grid.addWidget(pb_start, 3, 0, )  # 무언가를 시작하는 버튼
        grid.addWidget(pb_correction, 3, 1, )  # 틀린건 고칠때 사용하는 버튼
        grid.addWidget(pb_consonant, 0, 3)  # 자음으로 변환 버튼
        grid.addWidget(pb_vowels, 1, 3)  # 모음변환 버튼
        grid.addWidget(pb_number, 2, 3)  # 숫자 변환 버튼
        grid.addWidget(pb_up, 4, 0)  # 다음으로 넘어가는 화살표 버튼(ex: 숫자)
        grid.addWidget(pb_input, 4, 1)  # 숫자, 자음등 글장 입력 버튼
        grid.addWidget(pb_down, 4, 2)  # 전으로 넘어가는 화살표 버튼
        grid.addWidget(pb_enter, 3, 2)  #
        grid.addWidget(pb_cancel, 3, 3)  #

        lbl_display.setStyleSheet(
            "color: blue;" "background-color: #87CEFA;" "border-style: dashed;" "border-width: 3px;" "border-color: #1E90FF")

        # 키패드 크기 이름 구현
        self.setWindowTitle('시청각장애인_키패드')
        self.setGeometry(500, 200, 500, 500)
        self.show()

        # 버튼 눌렀을때 시그널
        pb_start.clicked.connect(start_c)  # 시작 버튼
        pb_up.clicked.connect(up_c)  # 위쪽 화살표
        pb_down.clicked.connect(down_c)  # 아래쪽 화살표
        pb_input.clicked.connect(input_c)  # 입력
        pb_cancel.clicked.connect(cancel_c)  # 취소
        pb_enter.clicked.connect(enter_c)  # 확인
        pb_correction.clicked.connect(cerrection_c)  # 정정
        pb_consonant.clicked.connect(consonant_c)  # 자음
        pb_number.clicked.connect(number_c)  # 숫자
        pb_vowels.clicked.connect(vowels_c)  # 모음


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
