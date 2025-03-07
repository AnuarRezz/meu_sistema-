from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.widget.setStyleSheet(
            "QPushButton#pushButton{"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.48, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));"
            "    color:rgba(255, 255, 255, 210);"
            "    border-radius:5px;"
            "}"
            "QPushButton#pushButton:hover{"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.48, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));"
            "}"
            "QPushButton#pushButton:pressed{"
            "    padding-left:5px; padding-top:5px;"
            "    background-color:rgba(105, 118, 132, 200);"
            "}"
        )
        self.widget.setObjectName("widget")
        
        # Imagem de fundo (opcional)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/background.png); border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        
        # Sobreposição para efeito escurecido
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.72, stop:0 rgba(0, 0, 0, 9), "
            "stop:0.38 rgba(0, 0, 0, 50), stop:0.84 rgba(0, 0, 0, 75));"
            "border-radius:20px;"
        )
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        
        # Painel central transparente
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100); border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        
        # Rótulo de título
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        
        # Campo para email (login)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0); border:none;"
            "border-bottom:2px solid rgba(105, 118, 132, 255);"
            "color:rgba(255, 255, 255, 230); padding-bottom:7px;"
        )
        self.lineEdit.setObjectName("lineEdit")
        
        # Campo para senha
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0); border:none;"
            "border-bottom:2px solid rgba(105, 118, 132, 255);"
            "color:rgba(255, 255, 255, 230); padding-bottom:7px;"
        )
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        # Botão de Login
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Rótulo opcional (ex: "Esqueceu a senha?")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(91, 358, 191, 21))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Senha"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_5.setText(_translate("Form", "Esqueceu a senha?"))
        # Preenche os campos com os dados para login
        self.lineEdit.setText("anuar")
        self.lineEdit_2.setText("123")
