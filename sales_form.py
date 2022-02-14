# -*- coding: utf-8 -*-
# Python Version: 3.8.6
# Sales Form Version: 2.3.1

# Imports PyQt5, sys, and platform for GUI, sqlite3 for SQL database, os for file paths
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3, os, platform

# Class containing functions for interacting with the sales_form.db file
class DatabaseAccess():
    # Initializes a connection to the sql database, adds a cursor for command execution, 
    # and creates a new table if one doesn't exist
    def __init__(self):
        self.sql_conn = self.createConnection("sales_form.db")
        self.sql_cursor = self.sql_conn.cursor()

        self.sql_cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sales'")
        if self.sql_cursor.fetchone()[0] != 1:
            self.sql_cursor.execute("CREATE TABLE sales (last_name, first_name, company, style, color, size, order_num, order_date, delivery_date, po_num, address, state, city, postal_code, phone_num, email, notes)")

    # Creates the connection with the sql database
    def createConnection(self, db_file):
        # Generates correct paths for program when frozen
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        db_path = os.path.join(application_path, db_file)
        try:
            conn = sqlite3.connect(db_path)
            return conn
        except sqlite3.Error as e:
            with open("sql_fail.txt", 'w') as sql_log:
                sql_log.write(str(e))
            sys.exit()

    # Adds a new set of data into the database
    def addCurrentData(self, data):
        for item in data:
            if item == "":
                data[data.index(item)] = "NULL"
        
        self.sql_cursor.execute(f"INSERT INTO sales VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', '{data[7]}', '{data[8]}', '{data[9]}', '{data[10]}', '{data[11]}', '{data[12]}', '{data[13]}', '{data[14]}', '{data[15]}', '{data[16]}')")
        self.sql_conn.commit()

    # Searches by order number for a item in the database
    # Displays either the first result in the GUI or a dialog if there are no results
    def search(self, order_num):
        self.sql_cursor.execute(f"SELECT * FROM sales WHERE order_num='{order_num}'")
        self.search_results = self.sql_cursor.fetchone()

        if self.search_results != None:
            if len(self.search_results) > 0:
                ui.displaySearchRes(self.search_results)
        else:
            self.Dialog = QtWidgets.QDialog()
            self.no_res_dialog = Ui_NoResDialog()
            self.no_res_dialog.setupUi(self.Dialog)
            self.Dialog.show()

    # Changes a current items data in the database (using order number)
    def modifyCurrentData(self, data):
        order_num = data[6]
        for item in data:
            if item == "":
                data[data.index(item)] = "NULL"

        self.sql_cursor.execute(f"UPDATE sales SET last_name='{data[0]}', first_name='{data[1]}', company='{data[2]}', style='{data[3]}', color='{data[4]}', size='{data[5]}', order_num='{data[6]}', order_date='{data[7]}', delivery_date='{data[8]}', po_num='{data[9]}', address='{data[10]}', state='{data[11]}', city='{data[12]}', postal_code='{data[13]}', phone_num='{data[14]}', email='{data[15]}', notes='{data[16]}' WHERE order_num='{order_num}'")
        self.sql_conn.commit()

        ui.modify_button.setEnabled(0)
        ui.delete_button.setEnabled(0)
        ui.clearDataFields()
        ui.displayUpdate(order_num)
 
    # Removes item from database using order number
    def removeCurrentData(self, order_num):
        self.sql_cursor.execute(f"DELETE FROM sales WHERE order_num='{order_num}'")
        self.sql_conn.commit()

# Class for the main app GUI
class Ui_MainWindow(object):
    # Builds GUI and adds all necesary widgets
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

        font = QtGui.QFont()
        font.setPointSize(15 - font_adjust)

        self.first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.first_name_label.setGeometry(QtCore.QRect(30, 100, 161, 21))
        self.first_name_label.setFont(font)
        self.first_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_field.setGeometry(QtCore.QRect(210, 100, 241, 22))
        self.first_name_field.setObjectName("first_name_field")

        self.last_Name_label = QtWidgets.QLabel(self.centralwidget)
        self.last_Name_label.setGeometry(QtCore.QRect(30, 140, 161, 21))
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
        self.company_label.setFont(font)
        self.company_label.setAlignment(QtCore.Qt.AlignCenter)
        self.company_label.setObjectName("company_label")

        self.company_field = QtWidgets.QLineEdit(self.centralwidget)
        self.company_field.setGeometry(QtCore.QRect(210, 180, 241, 22))
        self.company_field.setObjectName("company_field")

        self.style_label = QtWidgets.QLabel(self.centralwidget)
        self.style_label.setGeometry(QtCore.QRect(30, 230, 161, 21))
        self.style_label.setFont(font)
        self.style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.style_label.setObjectName("style_label")

        self.color_label = QtWidgets.QLabel(self.centralwidget)
        self.color_label.setGeometry(QtCore.QRect(30, 270, 161, 21))
        self.color_label.setFont(font)
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName("color_label")

        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(30, 310, 161, 21))
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
        self.order_num_label.setFont(font)
        self.order_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_num_label.setObjectName("order_num_label")

        self.order_date_label = QtWidgets.QLabel(self.centralwidget)
        self.order_date_label.setGeometry(QtCore.QRect(30, 400, 161, 21))
        self.order_date_label.setFont(font)
        self.order_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date_label.setObjectName("order_date_label")

        self.deliv_date_label = QtWidgets.QLabel(self.centralwidget)
        self.deliv_date_label.setGeometry(QtCore.QRect(30, 440, 161, 21))
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
        self.po_num_label.setFont(font)
        self.po_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.po_num_label.setObjectName("po_num_label")

        self.po_num_field = QtWidgets.QLineEdit(self.centralwidget)
        self.po_num_field.setGeometry(QtCore.QRect(210, 480, 241, 22))
        self.po_num_field.setObjectName("po_num_field")

        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(480, 100, 161, 21))
        self.address_label.setFont(font)
        self.address_label.setAlignment(QtCore.Qt.AlignCenter)
        self.address_label.setObjectName("address_label")

        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(480, 140, 161, 21))
        self.state_label.setFont(font)
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")

        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(480, 180, 161, 21))
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")

        self.postal_code_label = QtWidgets.QLabel(self.centralwidget)
        self.postal_code_label.setGeometry(QtCore.QRect(480, 220, 161, 21))
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
        for i in range(52):
            self.state_combobox.addItem("")

        self.phone_num_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_num_label.setGeometry(QtCore.QRect(480, 270, 161, 21))
        self.phone_num_label.setFont(font)
        self.phone_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_num_label.setObjectName("phone_num_label")

        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(480, 310, 161, 21))
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")

        self.notes_label = QtWidgets.QLabel(self.centralwidget)
        self.notes_label.setGeometry(QtCore.QRect(480, 360, 161, 21))
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

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QtCore.QRect(870, 40, 51, 21))

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

        # Modify counter allows for the save button to switch from adding data to updating data
        self.modify_counter = 0

        # Used to simplify some code with for loops rather than 17 individual limes
        self.field_list = [self.last_name_field, self.first_name_field,
            self.company_field, self.style_field, self.color_field,
            self.size_field, self.order_num_field, self.order_date_field, 
            self.deliv_date_field, self.po_num_field, self.address_field, 
            self.state_combobox, self.city_field, self.postal_code_field, 
            self.phone_num_field, self.email_field, self.notes_field]

        # Connects buttons to corresponding functions
        self.toolButton.clicked.connect(self.revertUi)
        self.clear_button.clicked.connect(self.clearFields)
        self.save_button.clicked.connect(self.saveCurrentFields)
        self.search_button.clicked.connect(self.searchDatabase)
        self.modify_button.clicked.connect(self.modifyAction)
        self.delete_button.clicked.connect(self.confirmDel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Sets texts for all widgets in the MainWindow
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

        self.states = ["", "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", 
            "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", 
            "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", 
            "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", 
            "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]
        for i in range(len(self.states)):
            self.state_combobox.setItemText(i, _translate("MainWindow", self.states[i]))

        self.phone_num_label.setText(_translate("MainWindow", "Customer Phone #:"))
        self.email_label.setText(_translate("MainWindow", "Customer Email:"))
        self.notes_label.setText(_translate("MainWindow", "Notes:"))

        self.toolButton.setText(_translate("MainWindow", "Revert"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.modify_button.setText(_translate("MainWindow", "Modify"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))

    # Reverts UI to original state (like restarting the program)
    def revertUi(self):
        self.enableFields(1)
        self.modify_button.setDisabled(1)
        self.delete_button.setDisabled(1)
        self.clear_button.setEnabled(1)
        self.save_button.setEnabled(1)
        self.modify_counter = 0
        self.clearDataFields()

    # Uses modify counter to determine with confirmatioon dialog is to be displayed
    def clearFields(self):
        self.Dialog = QtWidgets.QDialog()
        if self.modify_counter % 2 == 0:
            self.clear_confirm_dialog = Ui_ClConfirmDialog()
            self.clear_confirm_dialog.setupUi(self.Dialog)
            self.Dialog.show()
        else:
            self.clmod_confirm_dialog = Ui_ModConfirmDialog()
            self.clmod_confirm_dialog.setupUi(self.Dialog)
            self.Dialog.show()

    # Clears all text from GUI fields
    def clearDataFields(self):
        for item in self.field_list:
            if "QComboBox" not in str(type(item)):
                item.clear()
            else:
                item.setCurrentText("")

    # Launches confirm dialog for item deletion
    def confirmDel(self):
        self.Dialog = QtWidgets.QDialog()
        self.del_confirm_dialog = Ui_DelConfirmDialog()
        self.del_confirm_dialog.setupUi(self.Dialog)
        self.Dialog.show()

    # Calls for item deletion from the database and displays update afterwards
    def deleteEntry(self):
        order_num = self.order_num_field.text()
        dba.removeCurrentData(self.order_num_field.text())
        self.clearDataFields()
        self.modify_counter = 0
        self.modify_button.setDisabled(True)
        self.delete_button.setDisabled(True)

        self.Dialog = QtWidgets.QDialog()
        self.updated_dialog = Ui_UpdateDialog()
        self.updated_dialog.setupUi(self.Dialog, order_num)
        self.Dialog.show()

    # Creates list of current data and calls to either save or update the database
    def saveCurrentFields(self):
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
            self.phone_num_field.text(),
            self.email_field.text(),
            self.notes_field.toPlainText()
            ]

        if self.modify_counter % 2 == 0:
            dba.addCurrentData(self.data)
        else:
            dba.modifyCurrentData(self.data)

    # Creates search dialog 
    def searchDatabase(self):
        self.Dialog = QtWidgets.QDialog()
        self.search_dialog = Ui_SearchDialog()
        self.search_dialog.setupUi(self.Dialog)
        self.Dialog.show()

    # Displays results of search in MainWindow
    def displaySearchRes(self, search_results):
        for item in self.field_list:
            if type(item) is not type(QtWidgets.QComboBox()):
                item.setText(search_results[self.field_list.index(item)])
            else:
                item.setCurrentText(search_results[self.field_list.index(item)])

        # Disables modifcation of data and unlocks modify button
        self.enableFields(0)
        self.modify_button.setEnabled(1)
        self.save_button.setEnabled(0)
        self.clear_button.setEnabled(0)
        self.delete_button.setEnabled(0)
        self.modify_counter = 0

    # Enables or disables GUI fields
    def enableFields(self, id):
        for item in self.field_list:
            item.setEnabled(id)

    # Iterates modify counter and changes GUI accordingly
    def modifyAction(self):
        self.modify_counter += 1
        if self.modify_counter % 2 == 0:
            self.enableFields(0)
            self.save_button.setEnabled(0)
            self.clear_button.setEnabled(0)
            self.delete_button.setEnabled(0)
        else:
            self.enableFields(1)
            self.order_num_field.setDisabled(1)
            self.save_button.setEnabled(1)
            self.clear_button.setEnabled(1)
            self.delete_button.setEnabled(1)

    # Calls for dialog displaying that a database update/deletion has occured
    def displayUpdate(self, order_num):
        self.Dialog = QtWidgets.QDialog()
        self.updated_dialog = Ui_UpdateDialog()
        self.updated_dialog.setupUi(self.Dialog, order_num)
        self.Dialog.show()

# Dialog prompting user for order number to search
class Ui_SearchDialog(object):
    # Builds GUI and adds all necesary widgets
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

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Search", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"Order #:", None))

    # Calls for a database search using entered order number
    def accept(self):
        dba.search(self.lineEdit.text())
        ui.Dialog.close()

    # Closes Dialog
    def reject(self):
        ui.Dialog.close()

# Dialog promting user for confirmation on clearing the GUI fields
class Ui_ClConfirmDialog(object):
    # Builds GUI and adds all necesary widgets
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

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Clear Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will clear all data fields. Are you sure?", None))

    # Calls to clear all fields in the GUI
    def accept(self):
        ui.clearDataFields()
        ui.Dialog.close()

    # Closes Dialog
    def reject(self):
        ui.Dialog.close()

# Dialog promting user for confirmation on clearing the GUI fields while in modify mode
class Ui_ModConfirmDialog(object):
    # Builds GUI and adds all necesary widgets
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
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18 - font_adjust)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Clear Search Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will clear all data fields while you remain in modify mode. Are you sure?", None))

    # Calls to clear all fields in the GUI
    def accept(self):
        ui.clearDataFields()
        ui.order_num_field.setEnabled(1)
        ui.Dialog.close()

    # Closes Dialog
    def reject(self):
        ui.Dialog.close()

# Dialog promting user to comfirm deletion of database item
class Ui_DelConfirmDialog(object):
    # Builds GUI and adds all necesary widgets
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

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Delete Confirmation", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"This will remove this entry from the db. Are you sure?", None))

    # Calls to delete current item from database
    def accept(self):
        ui.deleteEntry()
        ui.Dialog.close()

    # Closes Dialog
    def reject(self):
        ui.Dialog.close()

class Ui_NoResDialog(object):
    # Builds GUI and adds all necesary widgets
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

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(250, 60, 81, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"No Search Result", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"No results found for that order number.", None))

    # Closes Dialog
    def accept(self):
        dba.Dialog.close()

class Ui_UpdateDialog(object):
    # Builds GUI and adds all necesary widgets
    def setupUi(self, Dialog, order_num):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(362, 98)
        Dialog.setMinimumSize(QtCore.QSize(362, 98))
        Dialog.setMaximumSize(QtCore.QSize(362, 98))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 38))
        font = QtGui.QFont()
        font.setPointSize(17 - font_adjust)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(250, 60, 81, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.retranslateUi(Dialog, order_num)

        # Connects buttonBox buttons to functions
        self.buttonBox.accepted.connect(self.accept)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Sets texts for all widgets in the Dialog
    def retranslateUi(self, Dialog, order_num):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Updated Database", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", f"The data for order number {order_num}\n was updated.", None))

    # Closes Dialog
    def accept(self):
        ui.Dialog.close()

if __name__ == "__main__":
    # If on windows adjust font to fit in GUI window
    if "Windows" in platform.platform():
        font_adjust = 5
    else:
        font_adjust = 0

    # Create amd show main app
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    dba = DatabaseAccess()

    MainWindow.show()

    # Close program on app exit
    sys.exit(app.exec_())