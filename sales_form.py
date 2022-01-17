# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sales_form_ui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from socket import create_connection
from tkinter import SEL_FIRST
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3
from sqlite3 import Error

class DatabaseAccess():
    def __init__(self):
        self.sql_conn = self.createConnection("database/sales_form.db")
        self.sql_cursor = self.sql_conn.cursor()
#        self.sql_cursor.execute("CREATE TABLE sales (last_name, first_name, comapny, style, color, size, order_num, order_date, delivery_date, po_num, address, state, city, postal_code, phone_num, email, notes)")

    def createConnection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)

    def add_current_data(self, last_name, first_name, comapny, style, color, size, order_num, order_date, delivery_date, po_num, address, state, city, postal_code, phone_num, email, notes):
        self.sql_cursor.execute(f"INSERT INTO sales VALUES ('{last_name}', '{first_name}', '{comapny}', '{style}', '{color}', '{size}', '{order_num}', '{order_date}', '{delivery_date}', '{po_num}', '{address}', '{state}', '{city}', '{postal_code}', '{phone_num}', '{email}', '{notes}')")
        self.sql_conn.commit()

    def search(self, order_num):
        self.sql_cursor.execute(f"SELECT * FROM sales WHERE order_num='{order_num}'")
        self.search_results = self.sql_cursor.fetchall()
        ui.display_search(self.search_results[0])

    def modify_current_data(self):
        pass

    def remove_current_data(self):
        pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 615)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sales_label = QtWidgets.QLabel(self.centralwidget)
        self.sales_label.setGeometry(QtCore.QRect(370, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sales_label.setFont(font)
        self.sales_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sales_label.setObjectName("sales_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 70, 921, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.first_name_label.setGeometry(QtCore.QRect(30, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.first_name_label.setFont(font)
        self.first_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_field.setGeometry(QtCore.QRect(210, 100, 241, 22))
        self.first_name_field.setObjectName("first_name_field")
        self.last_Name_label = QtWidgets.QLabel(self.centralwidget)
        self.last_Name_label.setGeometry(QtCore.QRect(30, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.last_Name_label.setFont(font)
        self.last_Name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.last_Name_label.setObjectName("last_Name_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 80, 16, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.last_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_field.setGeometry(QtCore.QRect(210, 140, 241, 22))
        self.last_name_field.setObjectName("last_name_field")
        self.company_label = QtWidgets.QLabel(self.centralwidget)
        self.company_label.setGeometry(QtCore.QRect(30, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.company_label.setFont(font)
        self.company_label.setAlignment(QtCore.Qt.AlignCenter)
        self.company_label.setObjectName("company_label")
        self.company_field = QtWidgets.QLineEdit(self.centralwidget)
        self.company_field.setGeometry(QtCore.QRect(210, 180, 241, 22))
        self.company_field.setObjectName("company_field")
        self.style_label = QtWidgets.QLabel(self.centralwidget)
        self.style_label.setGeometry(QtCore.QRect(30, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.style_label.setFont(font)
        self.style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.style_label.setObjectName("style_label")
        self.color_label = QtWidgets.QLabel(self.centralwidget)
        self.color_label.setGeometry(QtCore.QRect(30, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.color_label.setFont(font)
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName("color_label")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(30, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.size_label.setFont(font)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName("size_label")
        self.style_field = QtWidgets.QLineEdit(self.centralwidget)
        self.style_field.setGeometry(QtCore.QRect(210, 230, 241, 22))
        self.style_field.setObjectName("style_field")
        self.color_field = QtWidgets.QLineEdit(self.centralwidget)
        self.color_field.setGeometry(QtCore.QRect(210, 270, 241, 22))
        self.color_field.setObjectName("color_field")
        self.size_field = QtWidgets.QLineEdit(self.centralwidget)
        self.size_field.setGeometry(QtCore.QRect(210, 310, 241, 22))
        self.size_field.setObjectName("size_field")
        self.order_num_label = QtWidgets.QLabel(self.centralwidget)
        self.order_num_label.setGeometry(QtCore.QRect(30, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.order_num_label.setFont(font)
        self.order_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_num_label.setObjectName("order_num_label")
        self.order_date_label = QtWidgets.QLabel(self.centralwidget)
        self.order_date_label.setGeometry(QtCore.QRect(30, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.order_date_label.setFont(font)
        self.order_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date_label.setObjectName("order_date_label")
        self.deliv_date_label = QtWidgets.QLabel(self.centralwidget)
        self.deliv_date_label.setGeometry(QtCore.QRect(30, 440, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deliv_date_label.setFont(font)
        self.deliv_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deliv_date_label.setObjectName("deliv_date_label")
        self.order_num_field = QtWidgets.QLineEdit(self.centralwidget)
        self.order_num_field.setGeometry(QtCore.QRect(210, 360, 241, 22))
        self.order_num_field.setObjectName("order_num_field")
        self.order_date_field = QtWidgets.QLineEdit(self.centralwidget)
        self.order_date_field.setGeometry(QtCore.QRect(210, 400, 241, 22))
        self.order_date_field.setObjectName("order_date_field")
        self.deliv_date_field = QtWidgets.QLineEdit(self.centralwidget)
        self.deliv_date_field.setGeometry(QtCore.QRect(210, 440, 241, 22))
        self.deliv_date_field.setObjectName("deliv_date_field")
        self.po_num_label = QtWidgets.QLabel(self.centralwidget)
        self.po_num_label.setGeometry(QtCore.QRect(30, 480, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.po_num_label.setFont(font)
        self.po_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.po_num_label.setObjectName("po_num_label")
        self.po_num_field = QtWidgets.QLineEdit(self.centralwidget)
        self.po_num_field.setGeometry(QtCore.QRect(210, 480, 241, 22))
        self.po_num_field.setObjectName("po_num_field")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(480, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.address_label.setFont(font)
        self.address_label.setAlignment(QtCore.Qt.AlignCenter)
        self.address_label.setObjectName("address_label")
        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(480, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.state_label.setFont(font)
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(480, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.postal_code_label = QtWidgets.QLabel(self.centralwidget)
        self.postal_code_label.setGeometry(QtCore.QRect(480, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.postal_code_label.setFont(font)
        self.postal_code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.postal_code_label.setObjectName("postal_code_label")
        self.address_field = QtWidgets.QLineEdit(self.centralwidget)
        self.address_field.setGeometry(QtCore.QRect(650, 100, 271, 22))
        self.address_field.setObjectName("address_field")
        self.city_field = QtWidgets.QLineEdit(self.centralwidget)
        self.city_field.setGeometry(QtCore.QRect(650, 180, 271, 22))
        self.city_field.setObjectName("city_field")
        self.postal_code_field = QtWidgets.QLineEdit(self.centralwidget)
        self.postal_code_field.setGeometry(QtCore.QRect(650, 220, 271, 22))
        self.postal_code_field.setObjectName("postal_code_field")
        self.state_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.state_combobox.setGeometry(QtCore.QRect(650, 140, 81, 22))
        self.state_combobox.setObjectName("state_combobox")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.state_combobox.addItem("")
        self.phone_num_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_num_label.setGeometry(QtCore.QRect(480, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.phone_num_label.setFont(font)
        self.phone_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_num_label.setObjectName("phone_num_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(480, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.notes_label = QtWidgets.QLabel(self.centralwidget)
        self.notes_label.setGeometry(QtCore.QRect(480, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.notes_label.setFont(font)
        self.notes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notes_label.setObjectName("notes_label")
        self.notes_field = QtWidgets.QTextEdit(self.centralwidget)
        self.notes_field.setGeometry(QtCore.QRect(490, 390, 431, 111))
        self.notes_field.setObjectName("notes_field")
        self.phone_num_field = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_num_field.setGeometry(QtCore.QRect(650, 270, 271, 22))
        self.phone_num_field.setObjectName("phone_num_field")
        self.email_field = QtWidgets.QLineEdit(self.centralwidget)
        self.email_field.setGeometry(QtCore.QRect(650, 310, 271, 22))
        self.email_field.setObjectName("email_field")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 510, 921, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(780, 540, 131, 51))
        self.save_button.setObjectName("save_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(510, 540, 131, 51))
        self.clear_button.setObjectName("clear_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(40, 540, 131, 51))
        self.search_button.setObjectName("search_button")
        self.modify_button = QtWidgets.QPushButton(self.centralwidget)
        self.modify_button.setEnabled(False)
        self.modify_button.setGeometry(QtCore.QRect(220, 540, 131, 51))
        self.modify_button.setObjectName("modify_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.clear_button.clicked.connect(self.clear_fields)
        self.save_button.clicked.connect(self.save_fields)
        self.search_button.clicked.connect(self.search_db)
        self.modify_button.clicked.connect(self.modify_action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sales_label.setText(_translate("MainWindow", "Sales Form"))
        self.first_name_label.setText(_translate("MainWindow", "Customer First Name:"))
        self.last_Name_label.setText(_translate("MainWindow", "Customer Last Name:"))
        self.company_label.setText(_translate("MainWindow", "Customer Company:"))
        self.style_label.setText(_translate("MainWindow", "Style #:"))
        self.color_label.setText(_translate("MainWindow", "Color:"))
        self.size_label.setText(_translate("MainWindow", "Size:"))
        self.order_num_label.setText(_translate("MainWindow", "Order #:"))
        self.order_date_label.setText(_translate("MainWindow", "Order Date:"))
        self.deliv_date_label.setText(_translate("MainWindow", "Delivery Date:"))
        self.po_num_label.setText(_translate("MainWindow", "PO #:"))
        self.address_label.setText(_translate("MainWindow", "Customer Address:"))
        self.state_label.setText(_translate("MainWindow", "Customer State:"))
        self.city_label.setText(_translate("MainWindow", "Customer City:"))
        self.postal_code_label.setText(_translate("MainWindow", "Postal Code:"))
        self.state_combobox.setItemText(0, _translate("MainWindow", "AL"))
        self.state_combobox.setItemText(1, _translate("MainWindow", "AK"))
        self.state_combobox.setItemText(2, _translate("MainWindow", "AZ"))
        self.state_combobox.setItemText(3, _translate("MainWindow", "AR"))
        self.state_combobox.setItemText(4, _translate("MainWindow", "CA"))
        self.state_combobox.setItemText(5, _translate("MainWindow", "CO"))
        self.state_combobox.setItemText(6, _translate("MainWindow", "CT"))
        self.state_combobox.setItemText(7, _translate("MainWindow", "DE"))
        self.state_combobox.setItemText(8, _translate("MainWindow", "DC"))
        self.state_combobox.setItemText(9, _translate("MainWindow", "FL"))
        self.state_combobox.setItemText(10, _translate("MainWindow", "GA"))
        self.state_combobox.setItemText(11, _translate("MainWindow", "HI"))
        self.state_combobox.setItemText(12, _translate("MainWindow", "ID"))
        self.state_combobox.setItemText(13, _translate("MainWindow", "IL"))
        self.state_combobox.setItemText(14, _translate("MainWindow", "IN"))
        self.state_combobox.setItemText(15, _translate("MainWindow", "IA"))
        self.state_combobox.setItemText(16, _translate("MainWindow", "KS"))
        self.state_combobox.setItemText(17, _translate("MainWindow", "KY"))
        self.state_combobox.setItemText(18, _translate("MainWindow", "LA"))
        self.state_combobox.setItemText(19, _translate("MainWindow", "ME"))
        self.state_combobox.setItemText(20, _translate("MainWindow", "MD"))
        self.state_combobox.setItemText(21, _translate("MainWindow", "MA"))
        self.state_combobox.setItemText(22, _translate("MainWindow", "MI"))
        self.state_combobox.setItemText(23, _translate("MainWindow", "MN"))
        self.state_combobox.setItemText(24, _translate("MainWindow", "MS"))
        self.state_combobox.setItemText(25, _translate("MainWindow", "MO"))
        self.state_combobox.setItemText(26, _translate("MainWindow", "MT"))
        self.state_combobox.setItemText(27, _translate("MainWindow", "NB"))
        self.state_combobox.setItemText(28, _translate("MainWindow", "NV"))
        self.state_combobox.setItemText(29, _translate("MainWindow", "NH"))
        self.state_combobox.setItemText(30, _translate("MainWindow", "NJ"))
        self.state_combobox.setItemText(31, _translate("MainWindow", "NM"))
        self.state_combobox.setItemText(32, _translate("MainWindow", "NY"))
        self.state_combobox.setItemText(33, _translate("MainWindow", "NC"))
        self.state_combobox.setItemText(34, _translate("MainWindow", "ND"))
        self.state_combobox.setItemText(35, _translate("MainWindow", "OH"))
        self.state_combobox.setItemText(36, _translate("MainWindow", "OK"))
        self.state_combobox.setItemText(37, _translate("MainWindow", "OR"))
        self.state_combobox.setItemText(38, _translate("MainWindow", "PA"))
        self.state_combobox.setItemText(39, _translate("MainWindow", "PR"))
        self.state_combobox.setItemText(40, _translate("MainWindow", "RI"))
        self.state_combobox.setItemText(41, _translate("MainWindow", "SC"))
        self.state_combobox.setItemText(42, _translate("MainWindow", "SD"))
        self.state_combobox.setItemText(43, _translate("MainWindow", "TN"))
        self.state_combobox.setItemText(44, _translate("MainWindow", "TX"))
        self.state_combobox.setItemText(45, _translate("MainWindow", "UT"))
        self.state_combobox.setItemText(46, _translate("MainWindow", "VT"))
        self.state_combobox.setItemText(47, _translate("MainWindow", "VA"))
        self.state_combobox.setItemText(48, _translate("MainWindow", "WA"))
        self.state_combobox.setItemText(49, _translate("MainWindow", "WV"))
        self.state_combobox.setItemText(50, _translate("MainWindow", "WI"))
        self.state_combobox.setItemText(51, _translate("MainWindow", "WY"))
        self.phone_num_label.setText(_translate("MainWindow", "Customer Phone #:"))
        self.email_label.setText(_translate("MainWindow", "Customer Email:"))
        self.notes_label.setText(_translate("MainWindow", "Notes:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.modify_button.setText(_translate("MainWindow", "Modify"))

    def clear_fields(self):
        self.Dialog = QtWidgets.QDialog()
        self.confirm_dialog = Confirm_Dialog()
        self.confirm_dialog.setupUi(self.Dialog)
        self.Dialog.show()

    def save_fields(self):
        self.last_name = self.last_name_field.text()
        self.first_name = self.first_name_field.text()
        self.company = self.company_field.text()
        self.style = self.style_field.text()
        self.color = self.color_field.text()
        self.size = self.size_field.text()
        self.order_date = self.order_date_field.text()
        self.order_num = self.order_num_field.text()
        self.deliv_date = self.deliv_date_field.text()
        self.po_num = self.po_num_field.text()
        self.address = self.address_field.text()
        self.state = self.state_combobox.currentText()
        self.city = self.city_field.text()
        self.postal_code = self.postal_code_field.text()
        self.phone_num = self.phone_num_field.text()
        self.email = self.email_field.text()
        self.notes = self.notes_field.toPlainText()

        dba.add_current_data(self.last_name, self.first_name, self.company, self.style, self.color, self.size, self.order_num, self.order_date, self.deliv_date, self.po_num, self.address, self.state, self.city, self.postal_code, self.phone_num, self.email, self.notes)

    def search_db(self):
        self.Dialog = QtWidgets.QDialog()
        self.search_dialog = Search_Dialog()
        self.search_dialog.setupUi(self.Dialog)
        self.Dialog.show()

    def display_search(self, search_results):
        self.last_name_field.setText(search_results[0])
        self.first_name_field.setText(search_results[1])
        self.company_field.setText(search_results[2])
        self.style_field.setText(search_results[3])
        self.color_field.setText(search_results[4])
        self.size_field.setText(search_results[5])
        self.order_date_field.setText(search_results[6])
        self.order_num_field.setText(search_results[7])
        self.deliv_date_field.setText(search_results[8])
        self.po_num_field.setText(search_results[9])
        self.address_field.setText(search_results[10])
        self.state_combobox.setCurrentText(search_results[11])
        self.city_field.setText(search_results[12])
        self.postal_code_field.setText(search_results[13])
        self.phone_num_field.setText(search_results[14])
        self.email_field.setText(search_results[15])
        self.notes_field.setText(search_results[16])

        self.set_field_enabled(0)
        self.modify_button.setEnabled(1)
        self.save_button.setEnabled(0)
        self.modify_counter = 1

    def set_field_enabled(self, type):
        self.last_name_field.setEnabled(type)
        self.first_name_field.setEnabled(type)
        self.company_field.setEnabled(type)
        self.style_field.setEnabled(type)
        self.color_field.setEnabled(type)
        self.size_field.setEnabled(type)
        self.order_date_field.setEnabled(type)
        self.order_num_field.setEnabled(type)
        self.deliv_date_field.setEnabled(type)
        self.po_num_field.setEnabled(type)
        self.address_field.setEnabled(type)
        self.state_combobox.setEnabled(type)
        self.city_field.setEnabled(type)
        self.postal_code_field.setEnabled(type)
        self.phone_num_field.setEnabled(type)
        self.email_field.setEnabled(type)
        self.notes_field.setEnabled(type)

    def modify_action(self):
        if self.modify_counter % 2 == 0:
            self.set_field_enabled(0)
            self.save_button.setEnabled(0)
        elif self.modify_counter % 2 != 0:
            self.set_field_enabled(1)
            self.save_button.setEnabled(1)
        self.modify_counter += 1
        

class Search_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 90)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 221, 22))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Search", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"Order #:", None))

    def accept(self):
        self.order_num = self.lineEdit.text()
        dba.search(self.order_num)
        ui.Dialog.close()

    def reject(self):
        ui.Dialog.close()
    # retranslateUi

class Confirm_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Confirm")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(300, 150)
        Dialog.setMinimumSize(QtCore.QSize(300, 150))
        Dialog.setMaximumSize(QtCore.QSize(300, 150))
        Dialog.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 271, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.closeDialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmation"))

    def accept(self):
        self.clear_ui_fields()
        self.closeDialog()

    def clear_ui_fields(self):
        ui.first_name_field.clear()
        ui.last_name_field.clear()
        ui.company_field.clear()
        ui.style_field.clear()
        ui.color_field.clear()
        ui.size_field.clear()
        ui.order_date_field.clear()
        ui.order_num_field.clear()
        ui.deliv_date_field.clear()
        ui.po_num_field.clear()
        ui.address_field.clear()
        ui.city_field.clear()
        ui.postal_code_field.clear()
        ui.phone_num_field.clear()
        ui.email_field.clear()
        ui.notes_field.clear()

    def closeDialog(self):
        ui.Dialog.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    dba = DatabaseAccess()

    MainWindow.show()
    
    sys.exit(app.exec_())
