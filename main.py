from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys
from functionality import ConsultaExterna
import dbc

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Simple Storage Service")

        # Configurando menu Ativo
        self.icon_only_widget.hide()
        self.paginas.setCurrentWidget(self.pg_home)
        
        # Configurando botões menu
        self.btn_home_02.setChecked(True)

        

        ########################################################################################
        # Paginas do sistema

        # Menu retraido (Icon_only_widget)
        self.btn_home_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_cadastro_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_cadastro))
        self.btn_estoque_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_manuseio_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_manuseio))

        # Menu aberto (Full_menu_widget)
        self.btn_home_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_cadastro_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_cadastro))
        self.btn_estoque_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_manuseio_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_manuseio))
        ########################################################################################


        ########################################################################################
        # Preenchimento automatioco
        self.txt_cnpj.editingFinished.connect(self.consulta_cnpj)

        # registrar clientes
        self.btn_cadastrar_fornecedor.clicked.connect(self.registrar_empresa)

        # limpar campos
        self.btn_limpar_fornecedor.clicked.connect(self.limpar_campos)
        ########################################################################################

    # Criando consulta de api CNPJ
    def consulta_cnpj(self):
        # Criando conexão
        api = ConsultaExterna()
        request = api.pesquisar_cnpj(self.txt_cnpj.text())

        # Recuperando dados
        self.txt_nome.setText(request[0])
        self.txt_logradouro.setText(request[1])
        self.txt_numero.setText(request[2])
        self.txt_complemento.setText(request[3])
        self.txt_bairro.setText(request[4])
        self.txt_municipio.setText(request[5])
        self.txt_uf.setText(request[6])
        self.txt_cep.setText(request[7])
        self.txt_telefone.setText(request[8])
        self.txt_email.setText(request[9])

    def registrar_empresa(self):
        teste = dbc.DataBase()
        teste.cadastrar_fornecedor(self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(), 
                                   self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(),
                                     self.txt_uf.text(), self.txt_cep.text(), self.txt_telefone.text(), self.txt_email.text())
        self.limpar_campos()
        
    def limpar_campos(self):
        self.txt_cnpj.setText('')
        self.txt_nome.setText('')
        self.txt_logradouro.setText('')
        self.txt_numero.setText('')
        self.txt_complemento.setText('')
        self.txt_bairro.setText('')
        self.txt_municipio.setText('')
        self.txt_uf.setText('')
        self.txt_cep.setText('')
        self.txt_telefone.setText('')
        self.txt_email.setText('')
        




if __name__ == '__main__':

    app = QApplication(sys.argv)

    # loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()
    app.exec_()