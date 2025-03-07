from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, Qt, QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Nome de Usuário
        self.label_usuario = QLabel(self.centralwidget)
        self.label_usuario.setObjectName("label_usuario")
        font = QFont()
        font.setPointSize(16)
        self.label_usuario.setFont(font)
        self.label_usuario.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_usuario)
        
        self.lineEdit_usuario = QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.verticalLayout.addWidget(self.lineEdit_usuario)
        
        # CPF
        self.label_cpf = QLabel(self.centralwidget)
        self.label_cpf.setObjectName("label_cpf")
        self.label_cpf.setFont(font)
        self.label_cpf.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_cpf)
        
        self.lineEdit_cpf = QLineEdit(self.centralwidget)
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.verticalLayout.addWidget(self.lineEdit_cpf)
        
        # Email
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName("label_email")
        self.label_email.setFont(font)
        self.label_email.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_email)
        
        self.lineEdit_email = QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        
        # Endereço
        self.label_endereco = QLabel(self.centralwidget)
        self.label_endereco.setObjectName("label_endereco")
        self.label_endereco.setFont(font)
        self.label_endereco.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_endereco)
        
        self.lineEdit_endereco = QLineEdit(self.centralwidget)
        self.lineEdit_endereco.setObjectName("lineEdit_endereco")
        self.verticalLayout.addWidget(self.lineEdit_endereco)
        
        # Data de Nascimento
        self.label_data = QLabel(self.centralwidget)
        self.label_data.setObjectName("label_data")
        self.label_data.setFont(font)
        self.label_data.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_data)
        
        self.dateEdit_data = QDateEdit(self.centralwidget)
        self.dateEdit_data.setObjectName("dateEdit_data")
        self.dateEdit_data.setCalendarPopup(True)
        self.dateEdit_data.setDate(QDate.currentDate())
        self.verticalLayout.addWidget(self.dateEdit_data)
        
        # Contato
        self.label_contato = QLabel(self.centralwidget)
        self.label_contato.setObjectName("label_contato")
        self.label_contato.setFont(font)
        self.label_contato.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_contato)
        
        self.lineEdit_contato = QLineEdit(self.centralwidget)
        self.lineEdit_contato.setObjectName("lineEdit_contato")
        self.verticalLayout.addWidget(self.lineEdit_contato)
        
        # Botão de Cadastro
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButton.setFont(font2)
        self.verticalLayout.addWidget(self.pushButton)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Cadastro", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", "Nome de Usuário", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", "CPF", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", "Email", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", "Endereço", None))
        self.label_data.setText(QCoreApplication.translate("MainWindow", "Data de Nascimento", None))
        self.label_contato.setText(QCoreApplication.translate("MainWindow", "Contato", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Cadastrar", None))
