import sys
import math
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_clear_equal = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel()
        self.equation = QLineEdit()
        self.last_equation = ""

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("÷")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### =, clear, clearE, backspace, 역수, 제곱, 제곱근 나머지 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_clearE = QPushButton("CE")
        button_backspace = QPushButton("←")
        button_reciprocal = QPushButton("𝟏/𝒙")
        button_square = QPushButton("𝒙²")
        button_squareRoot = QPushButton("²√𝒙")
        button_remain = QPushButton("%")
        
        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가

        layout_number.addWidget(button_plus, 0, 3)
        layout_number.addWidget(button_minus, 1, 3)
        layout_number.addWidget(button_product, 2, 3)
        layout_number.addWidget(button_equal, 3, 3)

        ### =, clear, clearE, backspace, 역수, 제곱, 제곱근 나머지 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clearE.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_reciprocal.clicked.connect(self.button_reiprocal_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_squareRoot.clicked.connect(self.button_squareRoot_clicked)
        button_remain.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))

        ### =, clear, backspace, 역수, 제곱, 제곱근 나머지 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_remain, 0, 0)
        layout_clear_equal.addWidget(button_clearE, 0, 1)
        layout_clear_equal.addWidget(button_clear, 0, 2)
        layout_clear_equal.addWidget(button_backspace, 0, 3)
        layout_clear_equal.addWidget(button_reciprocal, 1, 0)
        layout_clear_equal.addWidget(button_square, 1, 1)
        layout_clear_equal.addWidget(button_squareRoot, 1, 2)
        layout_clear_equal.addWidget(button_division, 1, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 부호 변경 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("+/-")
        button_double_zero.clicked.connect(self.PlusMinus_button_clicked)
        layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def PlusMinus_button_clicked(self):
        equation = self.equation.text()
        equation = float(equation)
        equation *= -1
        equation = str(equation)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText("")
        self.last_equation = equation

    def button_equal_clicked(self, empty):
        equation = self.equation.text()
        equation = self.last_equation + equation
        solution = eval(equation)
        self.equation.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")

    def button_reiprocal_clicked(self):
        equation = self.equation.text()
        equation = float(equation)
        equation = pow(equation, -1) 
        equation = str(equation)
        self.equation.setText(equation)
  
    def button_square_clicked(self):
        equation = self.equation.text()
        equation = float(equation)
        equation = math.pow(equation, 2)
        equation = str(equation)
        self.equation.setText(equation)
 
    def button_squareRoot_clicked(self):
        equation = self.equation.text()
        equation = float(equation)
        equation = math.sqrt(equation)
        equation = str(equation)
        self.equation.setText(equation)

    def button_remain_clicked(self):
        equation = self.equation.text()
        equation = float(equation)
        equation = pow(equation, -1) 
        equation = str(equation)
        self.equation.setText(equation)

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())