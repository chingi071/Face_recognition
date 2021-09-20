import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from db_process import DBProcess

class DBWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self._ui = self._parent._ui

        if self._parent.bool_DBSaveButton_click == 0:
            self._ui.DBtext.setText("")

        self._ui.BrowseButton.clicked.connect(self.on_BrowseButton_clicked)
        self._ui.DBSaveButton.clicked.connect(self.on_DBSaveButton_clicked)
        self._ui.DBBackButton.clicked.connect(self.on_DBBackButton_clicked)

    # =====================================================
    def on_BrowseButton_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose the file", "./")
        if directory:
            if os.path.split(directory)[-1] == 'database':
                self._ui.DBtext.setText(directory)

            else:
                db_file_path = os.path.join(directory, 'database')
                self._ui.DBtext.setText(db_file_path)

    def on_DBSaveButton_clicked(self):
        if self._ui.DBtext.toPlainText() != "":
            self._parent.bool_DBSaveButton_click = 1
            db_file_path = self._ui.DBtext.toPlainText()

            if not os.path.exists(db_file_path):
                os.mkdir(db_file_path)

            db_sql_path = os.path.join(db_file_path, 'database.db')
            self.db_process = DBProcess(db_sql_path)

            message = QMessageBox.information(self, "Information", "The database has been successfully set!")

        else:
            message = QMessageBox.warning(self, "Warning!", "Please select the database path!")

    def on_DBBackButton_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(0)