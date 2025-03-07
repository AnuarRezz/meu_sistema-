import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Telas.LoginScreen import Ui_MainWindow as LoginUi
from Telas.CadastroScreen import Ui_MainWindow as CadastroUi
from Banco_de_dados.bd import verificar_usuario, adicionar_usuario

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginUi()
        self.ui.setupUi(self)
        # Preenche os campos de login com os dados "anuar" e "123"
        self.ui.lineEdit.setText("anuar")
        self.ui.lineEdit_2.setText("123")
        self.ui.pushButton.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        if verificar_usuario(usuario, senha):
            QMessageBox.information(self, "Login", "Login bem-sucedido!")
            # Neste exemplo, abriremos a tela de cadastro para demonstrar a navegação:
            self.abrir_cadastro()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

    def abrir_cadastro(self):
        self.cadastro_window = CadastroApp()
        self.cadastro_window.show()
        self.close()

class CadastroApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = CadastroUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cadastrar_usuario)

    def cadastrar_usuario(self):
        # Exemplo: usando os campos de email e contato para cadastro
        usuario = self.ui.lineEdit_email.text()  # ajuste conforme sua interface
        senha = self.ui.lineEdit_contato.text()    # ajuste conforme sua interface
        if usuario and senha:
            adicionar_usuario(usuario, senha)
            QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
            self.abrir_login()
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")

    def abrir_login(self):
        self.login_window = LoginApp()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())
