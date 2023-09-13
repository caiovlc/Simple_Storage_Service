# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'S3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(858, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_only_widget = QFrame(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(0, 100))
        self.icon_only_widget.setFrameShape(QFrame.StyledPanel)
        self.icon_only_widget.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.icon_only_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_logo_01 = QLabel(self.icon_only_widget)
        self.lbl_logo_01.setObjectName(u"lbl_logo_01")
        self.lbl_logo_01.setMinimumSize(QSize(50, 50))
        self.lbl_logo_01.setMaximumSize(QSize(50, 50))
        self.lbl_logo_01.setPixmap(QPixmap(u":/icons/icon/S3 icon.png"))
        self.lbl_logo_01.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.lbl_logo_01)

        self.btn_home_01 = QPushButton(self.icon_only_widget)
        self.btn_home_01.setObjectName(u"btn_home_01")
        icon = QIcon()
        icon.addFile(u":/icons/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icon/home-4-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_home_01.setIcon(icon)
        self.btn_home_01.setCheckable(True)
        self.btn_home_01.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_home_01)

        self.btn_cadastro_01 = QPushButton(self.icon_only_widget)
        self.btn_cadastro_01.setObjectName(u"btn_cadastro_01")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/note-2-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icon/note-2-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_cadastro_01.setIcon(icon1)
        self.btn_cadastro_01.setCheckable(True)
        self.btn_cadastro_01.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_cadastro_01)

        self.btn_estoque_01 = QPushButton(self.icon_only_widget)
        self.btn_estoque_01.setObjectName(u"btn_estoque_01")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icon/activity-feed-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_estoque_01.setIcon(icon2)
        self.btn_estoque_01.setCheckable(True)
        self.btn_estoque_01.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_estoque_01)

        self.btn_manuseio_01 = QPushButton(self.icon_only_widget)
        self.btn_manuseio_01.setObjectName(u"btn_manuseio_01")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icon/product-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_manuseio_01.setIcon(icon3)
        self.btn_manuseio_01.setCheckable(True)
        self.btn_manuseio_01.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_manuseio_01)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.icon_only_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/close-window-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icon/close-window-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 369, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.icon_only_widget)

        self.full_menu_widget = QFrame(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.full_menu_widget.setMinimumSize(QSize(140, 0))
        self.full_menu_widget.setMaximumSize(QSize(100, 16777215))
        self.full_menu_widget.setFrameShape(QFrame.StyledPanel)
        self.full_menu_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.lbl_logo_02 = QLabel(self.full_menu_widget)
        self.lbl_logo_02.setObjectName(u"lbl_logo_02")
        self.lbl_logo_02.setMinimumSize(QSize(50, 50))
        self.lbl_logo_02.setMaximumSize(QSize(50, 50))
        self.lbl_logo_02.setPixmap(QPixmap(u":/icons/icon/S3 icon.png"))
        self.lbl_logo_02.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lbl_logo_02)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.btn_home_02 = QPushButton(self.full_menu_widget)
        self.btn_home_02.setObjectName(u"btn_home_02")
        self.btn_home_02.setIcon(icon)
        self.btn_home_02.setCheckable(True)
        self.btn_home_02.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_home_02)

        self.btn_cadastro_02 = QPushButton(self.full_menu_widget)
        self.btn_cadastro_02.setObjectName(u"btn_cadastro_02")
        self.btn_cadastro_02.setIcon(icon1)
        self.btn_cadastro_02.setCheckable(True)
        self.btn_cadastro_02.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_cadastro_02)

        self.btn_estoque_02 = QPushButton(self.full_menu_widget)
        self.btn_estoque_02.setObjectName(u"btn_estoque_02")
        self.btn_estoque_02.setIcon(icon2)
        self.btn_estoque_02.setCheckable(True)
        self.btn_estoque_02.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_estoque_02)

        self.btn_manuseio_02 = QPushButton(self.full_menu_widget)
        self.btn_manuseio_02.setObjectName(u"btn_manuseio_02")
        self.btn_manuseio_02.setIcon(icon3)
        self.btn_manuseio_02.setCheckable(True)
        self.btn_manuseio_02.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_manuseio_02)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 367, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.full_menu_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.horizontalLayout_5.addWidget(self.full_menu_widget)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_menu = QPushButton(self.top_frame)
        self.toggle_menu.setObjectName(u"toggle_menu")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_menu.setIcon(icon5)
        self.toggle_menu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.toggle_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_pesquisa = QLineEdit(self.top_frame)
        self.input_pesquisa.setObjectName(u"input_pesquisa")

        self.horizontalLayout.addWidget(self.input_pesquisa)

        self.btn_pesquisa = QPushButton(self.top_frame)
        self.btn_pesquisa.setObjectName(u"btn_pesquisa")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisa.setIcon(icon6)

        self.horizontalLayout.addWidget(self.btn_pesquisa)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.toggle_menu.raise_()

        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.paginas = QStackedWidget(self.main_frame)
        self.paginas.setObjectName(u"paginas")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icon/S3 icon.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.paginas.addWidget(self.pg_home)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.horizontalLayout_9 = QHBoxLayout(self.pg_estoque)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.pg_estoque)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_9.addWidget(self.tableWidget)

        self.frame_9 = QFrame(self.pg_estoque)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_11)

        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_12)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.paginas.addWidget(self.pg_estoque)
        self.pg_manuseio = QWidget()
        self.pg_manuseio.setObjectName(u"pg_manuseio")
        self.verticalLayout_10 = QVBoxLayout(self.pg_manuseio)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget_2 = QTabWidget(self.pg_manuseio)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.Entrada = QWidget()
        self.Entrada.setObjectName(u"Entrada")
        self.verticalLayout_24 = QVBoxLayout(self.Entrada)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_7 = QSpacerItem(20, 84, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_7)

        self.frame_5 = QFrame(self.Entrada)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_21.addWidget(self.label_11)

        self.txt_sku_entrada = QLineEdit(self.frame_5)
        self.txt_sku_entrada.setObjectName(u"txt_sku_entrada")

        self.verticalLayout_21.addWidget(self.txt_sku_entrada)


        self.gridLayout_4.addLayout(self.verticalLayout_21, 0, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_22.addWidget(self.label_12)

        self.txt_tipo_entrada = QLineEdit(self.frame_5)
        self.txt_tipo_entrada.setObjectName(u"txt_tipo_entrada")

        self.verticalLayout_22.addWidget(self.txt_tipo_entrada)


        self.gridLayout_4.addLayout(self.verticalLayout_22, 0, 2, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_23.addWidget(self.label_13)

        self.cb_tamanho_entrada = QComboBox(self.frame_5)
        self.cb_tamanho_entrada.setObjectName(u"cb_tamanho_entrada")

        self.verticalLayout_23.addWidget(self.cb_tamanho_entrada)


        self.gridLayout_4.addLayout(self.verticalLayout_23, 0, 3, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_19.addWidget(self.label_15)

        self.spin_quantidade = QSpinBox(self.frame_5)
        self.spin_quantidade.setObjectName(u"spin_quantidade")

        self.verticalLayout_19.addWidget(self.spin_quantidade)


        self.gridLayout_4.addLayout(self.verticalLayout_19, 2, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_20.addWidget(self.label_14)

        self.txt_nome_entrada = QLineEdit(self.frame_5)
        self.txt_nome_entrada.setObjectName(u"txt_nome_entrada")

        self.verticalLayout_20.addWidget(self.txt_nome_entrada)


        self.gridLayout_4.addLayout(self.verticalLayout_20, 1, 0, 1, 4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.Entrada)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.btn_cadastrar_entrada = QPushButton(self.frame_6)
        self.btn_cadastrar_entrada.setObjectName(u"btn_cadastrar_entrada")

        self.horizontalLayout_6.addWidget(self.btn_cadastrar_entrada)

        self.btn_limpar_entrada = QPushButton(self.frame_6)
        self.btn_limpar_entrada.setObjectName(u"btn_limpar_entrada")

        self.horizontalLayout_6.addWidget(self.btn_limpar_entrada)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)


        self.verticalLayout_24.addWidget(self.frame_6)

        self.verticalSpacer_8 = QSpacerItem(20, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_8)

        self.tabWidget_2.addTab(self.Entrada, "")
        self.Saida = QWidget()
        self.Saida.setObjectName(u"Saida")
        self.verticalLayout_30 = QVBoxLayout(self.Saida)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_9 = QSpacerItem(20, 84, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_9)

        self.frame_7 = QFrame(self.Saida)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 2, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 2, 2, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_25.addWidget(self.label_16)

        self.txt_sku_saida = QLineEdit(self.frame_7)
        self.txt_sku_saida.setObjectName(u"txt_sku_saida")

        self.verticalLayout_25.addWidget(self.txt_sku_saida)


        self.gridLayout_5.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_27.addWidget(self.label_18)

        self.cb_tamanho_2 = QComboBox(self.frame_7)
        self.cb_tamanho_2.setObjectName(u"cb_tamanho_2")

        self.verticalLayout_27.addWidget(self.cb_tamanho_2)


        self.gridLayout_5.addLayout(self.verticalLayout_27, 0, 3, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_28.addWidget(self.label_19)

        self.spin_quantidade_saida = QSpinBox(self.frame_7)
        self.spin_quantidade_saida.setObjectName(u"spin_quantidade_saida")

        self.verticalLayout_28.addWidget(self.spin_quantidade_saida)


        self.gridLayout_5.addLayout(self.verticalLayout_28, 2, 0, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_29.addWidget(self.label_20)

        self.txt_nome_saida = QLineEdit(self.frame_7)
        self.txt_nome_saida.setObjectName(u"txt_nome_saida")

        self.verticalLayout_29.addWidget(self.txt_nome_saida)


        self.gridLayout_5.addLayout(self.verticalLayout_29, 1, 0, 1, 4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 2, 1, 1, 1)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_26.addWidget(self.label_17)

        self.txt_tipo_saida = QLineEdit(self.frame_7)
        self.txt_tipo_saida.setObjectName(u"txt_tipo_saida")

        self.verticalLayout_26.addWidget(self.txt_tipo_saida)


        self.gridLayout_5.addLayout(self.verticalLayout_26, 0, 2, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.Saida)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.btn_cadastrar_saida = QPushButton(self.frame_8)
        self.btn_cadastrar_saida.setObjectName(u"btn_cadastrar_saida")

        self.horizontalLayout_8.addWidget(self.btn_cadastrar_saida)

        self.btn_limpar_saida = QPushButton(self.frame_8)
        self.btn_limpar_saida.setObjectName(u"btn_limpar_saida")

        self.horizontalLayout_8.addWidget(self.btn_limpar_saida)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


        self.verticalLayout_30.addWidget(self.frame_8)

        self.verticalSpacer_10 = QSpacerItem(20, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_10)

        self.tabWidget_2.addTab(self.Saida, "")

        self.verticalLayout_10.addWidget(self.tabWidget_2)

        self.paginas.addWidget(self.pg_manuseio)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.fornecedor = QWidget()
        self.fornecedor.setObjectName(u"fornecedor")
        self.verticalLayout_11 = QVBoxLayout(self.fornecedor)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.frame = QFrame(self.fornecedor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 2)

        self.txt_cnpj = QLineEdit(self.frame)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_nome = QLineEdit(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_nome, 1, 1, 1, 3)

        self.txt_logradouro = QLineEdit(self.frame)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_logradouro, 2, 0, 1, 4)

        self.txt_numero = QLineEdit(self.frame)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_numero, 3, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_complemento, 3, 1, 1, 1)

        self.txt_bairro = QLineEdit(self.frame)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_bairro, 3, 2, 1, 2)

        self.txt_municipio = QLineEdit(self.frame)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_municipio, 4, 0, 1, 2)

        self.txt_uf = QLineEdit(self.frame)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_uf, 4, 2, 1, 1)

        self.txt_cep = QLineEdit(self.frame)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_cep, 4, 3, 1, 1)

        self.txt_telefone = QLineEdit(self.frame)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_telefone, 5, 0, 1, 2)

        self.txt_email = QLineEdit(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_email, 5, 2, 1, 2)


        self.verticalLayout_11.addWidget(self.frame)

        self.frame_2 = QFrame(self.fornecedor)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.btn_cadastrar_fornecedor = QPushButton(self.frame_2)
        self.btn_cadastrar_fornecedor.setObjectName(u"btn_cadastrar_fornecedor")

        self.horizontalLayout_3.addWidget(self.btn_cadastrar_fornecedor)

        self.btn_limpar_fornecedor = QPushButton(self.frame_2)
        self.btn_limpar_fornecedor.setObjectName(u"btn_limpar_fornecedor")

        self.horizontalLayout_3.addWidget(self.btn_limpar_fornecedor)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_18)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.fornecedor, "")
        self.produto = QWidget()
        self.produto.setObjectName(u"produto")
        self.verticalLayout_18 = QVBoxLayout(self.produto)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_5 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.label_4 = QLabel(self.produto)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_18.addWidget(self.label_4)

        self.frame_3 = QFrame(self.produto)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(203, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 3, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5)

        self.txt_sku_produto = QLineEdit(self.frame_3)
        self.txt_sku_produto.setObjectName(u"txt_sku_produto")

        self.verticalLayout_12.addWidget(self.txt_sku_produto)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 0, 1, 2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_14.addWidget(self.label_7)

        self.txt_cnpj_fornecedor_02 = QLineEdit(self.frame_3)
        self.txt_cnpj_fornecedor_02.setObjectName(u"txt_cnpj_fornecedor_02")

        self.verticalLayout_14.addWidget(self.txt_cnpj_fornecedor_02)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 2, 4, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9)

        self.spin_custo = QDoubleSpinBox(self.frame_3)
        self.spin_custo.setObjectName(u"spin_custo")

        self.verticalLayout_16.addWidget(self.spin_custo)


        self.gridLayout_2.addLayout(self.verticalLayout_16, 4, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6)

        self.cb_tipo = QComboBox(self.frame_3)
        self.cb_tipo.setObjectName(u"cb_tipo")

        self.verticalLayout_13.addWidget(self.cb_tipo)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 2, 6, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_15.addWidget(self.label_8)

        self.txt_produto = QLineEdit(self.frame_3)
        self.txt_produto.setObjectName(u"txt_produto")

        self.verticalLayout_15.addWidget(self.txt_produto)


        self.gridLayout_2.addLayout(self.verticalLayout_15, 3, 0, 1, 7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10)

        self.spin_preco = QDoubleSpinBox(self.frame_3)
        self.spin_preco.setObjectName(u"spin_preco")

        self.verticalLayout_17.addWidget(self.spin_preco)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 4, 1, 1, 2)


        self.verticalLayout_18.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.produto)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.btn_cadastrar_produto = QPushButton(self.frame_4)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")

        self.horizontalLayout_4.addWidget(self.btn_cadastrar_produto)

        self.btn_limpar_produto = QPushButton(self.frame_4)
        self.btn_limpar_produto.setObjectName(u"btn_limpar_produto")

        self.horizontalLayout_4.addWidget(self.btn_limpar_produto)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)


        self.verticalLayout_18.addWidget(self.frame_4)

        self.verticalSpacer_6 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)

        self.tabWidget.addTab(self.produto, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.paginas.addWidget(self.pg_cadastro)

        self.verticalLayout_4.addWidget(self.paginas)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.footer_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout_5.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toggle_menu.toggled.connect(self.icon_only_widget.setVisible)
        self.toggle_menu.toggled.connect(self.full_menu_widget.setHidden)
        self.btn_home_01.toggled.connect(self.btn_home_02.setChecked)
        self.btn_cadastro_01.toggled.connect(self.btn_cadastro_02.setChecked)
        self.btn_estoque_01.toggled.connect(self.btn_estoque_02.setChecked)
        self.btn_manuseio_01.toggled.connect(self.btn_manuseio_02.setChecked)
        self.btn_home_02.toggled.connect(self.btn_home_01.setChecked)
        self.btn_cadastro_02.toggled.connect(self.btn_cadastro_01.setChecked)
        self.btn_estoque_02.toggled.connect(self.btn_estoque_01.setChecked)
        self.btn_manuseio_02.toggled.connect(self.btn_manuseio_01.setChecked)
        self.pushButton_5.toggled.connect(self.pushButton_10.setChecked)
        self.pushButton_10.toggled.connect(self.pushButton_5.setChecked)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_10.clicked.connect(MainWindow.close)

        self.paginas.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_logo_01.setText("")
        self.btn_home_01.setText("")
        self.btn_cadastro_01.setText("")
        self.btn_estoque_01.setText("")
        self.btn_manuseio_01.setText("")
        self.pushButton_5.setText("")
        self.lbl_logo_02.setText("")
        self.btn_home_02.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro_02.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_estoque_02.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_manuseio_02.setText(QCoreApplication.translate("MainWindow", u"Manuseio", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.toggle_menu.setText("")
        self.input_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search..", None))
        self.btn_pesquisa.setText("")
        self.label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SKU", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TAMANHO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sku:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.btn_cadastrar_entrada.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_limpar_entrada.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Entrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sku:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.btn_cadastrar_saida.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_limpar_saida.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Saida), QCoreApplication.translate("MainWindow", u"Saida", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastro de Fornecedores</p></body></html>", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.btn_cadastrar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_limpar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fornecedor), QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastro de Produto</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sku:", None))
        self.txt_sku_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Sku Produto", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fornecedor:", None))
        self.txt_cnpj_fornecedor_02.setPlaceholderText(QCoreApplication.translate("MainWindow", u" CNPJ Fornecedor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Custo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.cb_tipo.setCurrentText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.txt_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Produto", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de venda", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_limpar_produto.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.produto), QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CopyRight by 4C version.1", None))
    # retranslateUi

