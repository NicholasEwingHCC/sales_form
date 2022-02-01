# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3, os, platform

if "Windows" in platform.platform():
    font_adjust = 5
else:
    font_adjust = 0

class DatabaseAccess():
    def __init__(self):
        self.sql_conn = self.createConnection("sales_form.db")
        self.sql_cursor = self.sql_conn.cursor()
        self.sql_cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sales'")
        if self.sql_cursor.fetchone()[0] == 1:
            #print("Sales table exists.")
            pass
        else:
            self.sql_cursor.execute("CREATE TABLE sales (last_name, first_name, company, style, color, size, order_num, order_date, delivery_date, po_num, address, state, city, postal_code, phone_num, email, notes)")

    def createConnection(self, db_file):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        db_path = os.path.join(application_path, db_file)
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            #print(sqlite3.version)
            return conn
        except sqlite3.Error as e:
            #print(e)
            sys.exit()

    def add_current_data(self, data):
        for value in data:
            if value == "":
                data[data.index(value)] = "NULL"
        self.sql_cursor.execute(f"INSERT INTO sales VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', '{data[7]}', '{data[8]}', '{data[9]}', '{data[10]}', '{data[11]}', '{data[12]}', '{data[13]}', '{data[14]}', '{data[15]}', '{data[16]}')")
        self.sql_conn.commit()

    def search(self, order_num):
        self.sql_cursor.execute(f"SELECT * FROM sales WHERE order_num='{order_num}'")
        self.search_results = self.sql_cursor.fetchall()
        if len(self.search_results) > 0:
            ui.display_search(self.search_results[0])
        else:
            self.Dialog = QtWidgets.QDialog()
            self.no_res_dialog = Ui_No_Res_Dialog()
            self.no_res_dialog.setupUi(self.Dialog)
            self.Dialog.show()
            #print("No search results for that order number")

    def modify_current_data(self, data):
        order_num = data[6]
        for value in data:
            if value == "":
                data[data.index(value)] = "NULL"
        self.sql_cursor.execute(f"UPDATE sales SET last_name='{data[0]}', first_name='{data[1]}', company='{data[2]}', style='{data[3]}', color='{data[4]}', size='{data[5]}', order_num='{data[6]}', order_date='{data[7]}', delivery_date='{data[8]}', po_num='{data[9]}', address='{data[10]}', state='{data[11]}', city='{data[12]}', postal_code='{data[13]}', phone_num='{data[14]}', email='{data[15]}', notes='{data[16]}' WHERE order_num='{order_num}'")
        self.sql_conn.commit()
        ui.modify_button.setEnabled(0)
        ui.delete_button.setEnabled(0)
        ui.clear_ui_fields()

    def remove_current_data(self, data):
        self.sql_cursor.execute(f"DELETE FROM sales WHERE order_num='{data}'")
        self.sql_conn.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 615)
        MainWindow.setMinimumSize(QtCore.QSize(943, 615))
        MainWindow.setMaximumSize(QtCore.QSize(943, 615))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sales_label = QtWidgets.QLabel(self.centralwidget)
        self.sales_label.setGeometry(QtCore.QRect(370, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(32 - font_adjust)
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
        font.setPointSize(15 - font_adjust)
        self.first_name_label.setFont(font)
        self.first_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_field.setGeometry(QtCore.QRect(210, 100, 241, 22))
        self.first_name_field.setObjectName("first_name_field")
        self.last_Name_label = QtWidgets.QLabel(self.centralwidget)
        self.last_Name_label.setGeometry(QtCore.QRect(30, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        font.setPointSize(15 - font_adjust)
        self.company_label.setFont(font)
        self.company_label.setAlignment(QtCore.Qt.AlignCenter)
        self.company_label.setObjectName("company_label")
        self.company_field = QtWidgets.QLineEdit(self.centralwidget)
        self.company_field.setGeometry(QtCore.QRect(210, 180, 241, 22))
        self.company_field.setObjectName("company_field")
        self.style_label = QtWidgets.QLabel(self.centralwidget)
        self.style_label.setGeometry(QtCore.QRect(30, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.style_label.setFont(font)
        self.style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.style_label.setObjectName("style_label")
        self.color_label = QtWidgets.QLabel(self.centralwidget)
        self.color_label.setGeometry(QtCore.QRect(30, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.color_label.setFont(font)
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName("color_label")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(30, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        font.setPointSize(15 - font_adjust)
        self.order_num_label.setFont(font)
        self.order_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_num_label.setObjectName("order_num_label")
        self.order_date_label = QtWidgets.QLabel(self.centralwidget)
        self.order_date_label.setGeometry(QtCore.QRect(30, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.order_date_label.setFont(font)
        self.order_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date_label.setObjectName("order_date_label")
        self.deliv_date_label = QtWidgets.QLabel(self.centralwidget)
        self.deliv_date_label.setGeometry(QtCore.QRect(30, 440, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        font.setPointSize(15 - font_adjust)
        self.po_num_label.setFont(font)
        self.po_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.po_num_label.setObjectName("po_num_label")
        self.po_num_field = QtWidgets.QLineEdit(self.centralwidget)
        self.po_num_field.setGeometry(QtCore.QRect(210, 480, 241, 22))
        self.po_num_field.setObjectName("po_num_field")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(480, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.address_label.setFont(font)
        self.address_label.setAlignment(QtCore.Qt.AlignCenter)
        self.address_label.setObjectName("address_label")
        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(480, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.state_label.setFont(font)
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(480, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.postal_code_label = QtWidgets.QLabel(self.centralwidget)
        self.postal_code_label.setGeometry(QtCore.QRect(480, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        self.state_combobox.addItem("")
        self.phone_num_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_num_label.setGeometry(QtCore.QRect(480, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.phone_num_label.setFont(font)
        self.phone_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_num_label.setObjectName("phone_num_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(480, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.notes_label = QtWidgets.QLabel(self.centralwidget)
        self.notes_label.setGeometry(QtCore.QRect(480, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        self.clear_button.setGeometry(QtCore.QRect(560, 540, 131, 51))
        self.clear_button.setObjectName("clear_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(40, 540, 131, 51))
        self.search_button.setObjectName("search_button")
        self.modify_button = QtWidgets.QPushButton(self.centralwidget)
        self.modify_button.setEnabled(False)
        self.modify_button.setGeometry(QtCore.QRect(190, 540, 131, 51))
        self.modify_button.setObjectName("modify_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setEnabled(False)
        self.delete_button.setGeometry(QtCore.QRect(410, 540, 131, 51))
        self.delete_button.setObjectName("delete_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.modify_counter = 0

        self.clear_button.clicked.connect(self.clear_fields)
        self.save_button.clicked.connect(self.save_fields)
        self.search_button.clicked.connect(self.search_db)
        self.modify_button.clicked.connect(self.modify_action)
        self.delete_button.clicked.connect(self.del_confirm)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sales Form App"))
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
        self.state_combobox.setItemText(0, _translate("MainWindow", ""))
        self.state_combobox.setItemText(1, _translate("MainWindow", "AL"))
        self.state_combobox.setItemText(2, _translate("MainWindow", "AK"))
        self.state_combobox.setItemText(3, _translate("MainWindow", "AZ"))
        self.state_combobox.setItemText(4, _translate("MainWindow", "AR"))
        self.state_combobox.setItemText(5, _translate("MainWindow", "CA"))
        self.state_combobox.setItemText(6, _translate("MainWindow", "CO"))
        self.state_combobox.setItemText(7, _translate("MainWindow", "CT"))
        self.state_combobox.setItemText(8, _translate("MainWindow", "DE"))
        self.state_combobox.setItemText(9, _translate("MainWindow", "DC"))
        self.state_combobox.setItemText(10, _translate("MainWindow", "FL"))
        self.state_combobox.setItemText(11, _translate("MainWindow", "GA"))
        self.state_combobox.setItemText(12, _translate("MainWindow", "HI"))
        self.state_combobox.setItemText(13, _translate("MainWindow", "ID"))
        self.state_combobox.setItemText(14, _translate("MainWindow", "IL"))
        self.state_combobox.setItemText(15, _translate("MainWindow", "IN"))
        self.state_combobox.setItemText(16, _translate("MainWindow", "IA"))
        self.state_combobox.setItemText(17, _translate("MainWindow", "KS"))
        self.state_combobox.setItemText(18, _translate("MainWindow", "KY"))
        self.state_combobox.setItemText(19, _translate("MainWindow", "LA"))
        self.state_combobox.setItemText(20, _translate("MainWindow", "ME"))
        self.state_combobox.setItemText(21, _translate("MainWindow", "MD"))
        self.state_combobox.setItemText(22, _translate("MainWindow", "MA"))
        self.state_combobox.setItemText(23, _translate("MainWindow", "MI"))
        self.state_combobox.setItemText(24, _translate("MainWindow", "MN"))
        self.state_combobox.setItemText(25, _translate("MainWindow", "MS"))
        self.state_combobox.setItemText(26, _translate("MainWindow", "MO"))
        self.state_combobox.setItemText(27, _translate("MainWindow", "MT"))
        self.state_combobox.setItemText(28, _translate("MainWindow", "NB"))
        self.state_combobox.setItemText(29, _translate("MainWindow", "NV"))
        self.state_combobox.setItemText(30, _translate("MainWindow", "NH"))
        self.state_combobox.setItemText(31, _translate("MainWindow", "NJ"))
        self.state_combobox.setItemText(32, _translate("MainWindow", "NM"))
        self.state_combobox.setItemText(33, _translate("MainWindow", "NY"))
        self.state_combobox.setItemText(34, _translate("MainWindow", "NC"))
        self.state_combobox.setItemText(35, _translate("MainWindow", "ND"))
        self.state_combobox.setItemText(36, _translate("MainWindow", "OH"))
        self.state_combobox.setItemText(37, _translate("MainWindow", "OK"))
        self.state_combobox.setItemText(38, _translate("MainWindow", "OR"))
        self.state_combobox.setItemText(39, _translate("MainWindow", "PA"))
        self.state_combobox.setItemText(40, _translate("MainWindow", "PR"))
        self.state_combobox.setItemText(41, _translate("MainWindow", "RI"))
        self.state_combobox.setItemText(42, _translate("MainWindow", "SC"))
        self.state_combobox.setItemText(43, _translate("MainWindow", "SD"))
        self.state_combobox.setItemText(44, _translate("MainWindow", "TN"))
        self.state_combobox.setItemText(45, _translate("MainWindow", "TX"))
        self.state_combobox.setItemText(46, _translate("MainWindow", "UT"))
        self.state_combobox.setItemText(47, _translate("MainWindow", "VT"))
        self.state_combobox.setItemText(48, _translate("MainWindow", "VA"))
        self.state_combobox.setItemText(49, _translate("MainWindow", "WA"))
        self.state_combobox.setItemText(50, _translate("MainWindow", "WV"))
        self.state_combobox.setItemText(51, _translate("MainWindow", "WI"))
        self.state_combobox.setItemText(52, _translate("MainWindow", "WY"))
        self.phone_num_label.setText(_translate("MainWindow", "Customer Phone #:"))
        self.email_label.setText(_translate("MainWindow", "Customer Email:"))
        self.notes_label.setText(_translate("MainWindow", "Notes:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.modify_button.setText(_translate("MainWindow", "Modify"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))

    def clear_fields(self):
        if self.modify_counter % 2 == 0:
            self.Dialog = QtWidgets.QDialog()
            self.confirm_dialog = Confirm_Dialog()
            self.confirm_dialog.setupUi(self.Dialog)
            self.Dialog.show()
        elif self.modify_counter % 2 != 0:
            self.Dialog = QtWidgets.QDialog()
            self.confirm_dialog = Confirm_Mod_Dialog()
            self.confirm_dialog.setupUi(self.Dialog)
            self.Dialog.show()

    def clear_ui_fields(self):
        self.first_name_field.clear()
        self.last_name_field.clear()
        self.company_field.clear()
        self.style_field.clear()
        self.color_field.clear()
        self.size_field.clear()
        self.order_date_field.clear()
        self.order_num_field.clear()
        self.deliv_date_field.clear()
        self.po_num_field.clear()
        self.address_field.clear()
        self.state_combobox.setCurrentText("")
        self.city_field.clear()
        self.postal_code_field.clear()
        self.phone_num_field.clear()
        self.email_field.clear()
        self.notes_field.clear()

    def del_confirm(self):
        self.Dialog = QtWidgets.QDialog()
        self.confirm_dialog = Confirm_Del_Dialog()
        self.confirm_dialog.setupUi(self.Dialog)
        self.Dialog.show()

    def delete_entry(self):
        data = self.order_num_field.text()
        dba.remove_current_data(data)
        self.clear_ui_fields()
        self.modify_counter = 0
        #print("ui.delete_entry > " + str(self.modify_counter))
        self.modify_button.setEnabled(False)
        self.delete_button.setEnabled(False)

    def save_fields(self):
        self.data = [
            self.last_name_field.text(),
            self.first_name_field.text(),
            self.company_field.text(),
            self.style_field.text(),
            self.color_field.text(),
            self.size_field.text(),
            self.order_num_field.text(),
            self.order_date_field.text(),
            self.deliv_date_field.text(),
            self.po_num_field.text(),
            self.address_field.text(),
            self.state_combobox.currentText(),
            self.city_field.text(),
            self.postal_code_field.text(),
            self.notes_field.toPlainText(),
            self.phone_num_field.text(),
            self.email_field.text()
        ]

        if self.modify_counter % 2 == 0:
            dba.add_current_data(self.data)
            #print("Added with value 0")
        elif self.modify_counter % 2 != 0:
            dba.modify_current_data(self.data)
            #print("Modified with value 1")

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
        self.order_num_field.setText(search_results[6])
        self.order_date_field.setText(search_results[7])
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
        self.clear_button.setEnabled(0)
        self.delete_button.setEnabled(0)
        self.modify_counter = 0
        #print("ui.display_search > " + str(self.modify_counter))

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
        self.modify_counter += 1
        #print("ui.modify_action > " + str(self.modify_counter))
        if self.modify_counter % 2 == 0:
            self.set_field_enabled(0)
            self.save_button.setEnabled(0)
            self.clear_button.setEnabled(0)
            self.delete_button.setEnabled(0)
        elif self.modify_counter % 2 != 0:
            self.set_field_enabled(1)
            self.save_button.setEnabled(1)
            self.clear_button.setEnabled(1)
            self.delete_button.setEnabled(1)
        

class Search_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 90)
        Dialog.setMinimumSize(QtCore.QSize(320, 90))
        Dialog.setMaximumSize(QtCore.QSize(320, 90))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)
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
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(271, 127)
        Dialog.setMinimumSize(QtCore.QSize(271, 127))
        Dialog.setMaximumSize(QtCore.QSize(271, 127))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18 - font_adjust)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.closeDialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Clear Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will clear all data fields. Are you sure?", None))
    # retranslateUi

    def accept(self):
        self.clear_ui_fields()
        #print("Confrim_Dialog.accept > " + str(ui.modify_counter))
        self.closeDialog()

    def clear_ui_fields(self):
        ui.clear_ui_fields()

    def closeDialog(self):
        ui.Dialog.close()

class Confirm_Mod_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(271, 127)
        Dialog.setMinimumSize(QtCore.QSize(271, 127))
        Dialog.setMaximumSize(QtCore.QSize(271, 127))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18 - font_adjust)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.closeDialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Clear Search Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will clear all data fields. Are you sure?", None))
    # retranslateUi

    def accept(self):
        self.clear_ui_fields()
#        ui.modify_button.setEnabled(0)
#        ui.delete_button.setEnabled(0)
        #print("Confrim_Mod_Dialog.accept > " + str(ui.modify_counter))
        self.closeDialog()

    def clear_ui_fields(self):
        ui.clear_ui_fields()

    def closeDialog(self):
        ui.Dialog.close()

class Confirm_Del_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(271, 127)
        Dialog.setMinimumSize(QtCore.QSize(271, 127))
        Dialog.setMaximumSize(QtCore.QSize(271, 127))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18 - font_adjust)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.closeDialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Delete Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will remove this entry from the db. Are you sure?", None))
    # retranslateUi

    def accept(self):
        ui.delete_entry()
        self.closeDialog()

    def closeDialog(self):
        ui.Dialog.close()

class Ui_No_Res_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(362, 98)
        Dialog.setMinimumSize(QtCore.QSize(362, 98))
        Dialog.setMaximumSize(QtCore.QSize(362, 98))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(17 - font_adjust)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(250, 60, 81, 26))

        self.retranslateUi(Dialog)

        self.pushButton.clicked.connect(self.accept)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"No Search Result", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"No results found for that order number.", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

    def accept(self):
        dba.Dialog.close()

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle('Fusion')
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        dba = DatabaseAccess()

        MainWindow.show()
        
    except Exception as e:
        print(str(e))
        with open("log.txt", 'w') as log_file:
            log_file.write(str(e))
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage("Program failed... Send log.txt file to ewingnjole@gmail.com")
        error_dialog.show()
        
    sys.exit(app.exec_())
