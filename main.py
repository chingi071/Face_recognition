import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window_ui import Ui_MainWindow
from camera_widget import CameraWidget
from db_widget import DBWidget
from recognize_process import RecogProcess
from recognize_widget import RecogWidget
from iconqrc import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowTitle('Face Recognition')

        self.recognize_process = RecogProcess()

        self.bool_DBSaveButton_click = 0
        self.db_widget = DBWidget(self)

        # set pushbutton color
        stylesheet = "QPushButton {background: #E6CAFF}"
        self._ui.DBSetButton.setStyleSheet(stylesheet)
        self._ui.PhotoButton.setStyleSheet(stylesheet)
        self._ui.LoadButton.setStyleSheet(stylesheet)
        self._ui.RecogButton.setStyleSheet(stylesheet)
        self._ui.BrowseButton.setStyleSheet(stylesheet)
        self._ui.DBSaveButton.setStyleSheet(stylesheet)
        self._ui.DBBackButton.setStyleSheet(stylesheet)
        self._ui.CaptureButton.setStyleSheet(stylesheet)
        self._ui.ChooseButton.setStyleSheet(stylesheet)
        self._ui.SaveButton.setStyleSheet(stylesheet)
        self._ui.BackButton.setStyleSheet(stylesheet)
        self._ui.RecogStartButton.setStyleSheet(stylesheet)
        self._ui.RecogBackButton.setStyleSheet(stylesheet)

    # =====================================================
    def paintEvent(self, event):
        painter = QPainter(self)
        image = QPixmap(':/pix/background.jpg')
        rect = QRect(0, 0, 1000, 800)
        painter.drawPixmap(rect, image)
    # =====================================================
    @pyqtSlot()
    def on_DBSetButton_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(1)

    @pyqtSlot()
    def on_PhotoButton_clicked(self):
        if self._ui.DBtext.toPlainText() != "":
            self._ui.stackedWidget.setCurrentIndex(2)
            self._ui.CameraWidget.setCurrentIndex(0)
            self._ui.ButtonWidget.setCurrentIndex(0)
            self._ui.CaptureButton.setText("Take a picture")
            self.camera_widget = CameraWidget(self)

        else:
            message = QMessageBox.warning(self, "Warning!", "Please select the database path!")

    @pyqtSlot()
    def on_LoadButton_clicked(self):
        if self._ui.DBtext.toPlainText() != "":
            self._ui.stackedWidget.setCurrentIndex(2)
            self._ui.CameraWidget.setCurrentIndex(2)
            self._ui.ButtonWidget.setCurrentIndex(1)
            self._ui.ChooseImage.setPixmap(QPixmap(""))
            self.camera_widget = CameraWidget(self)

        else:
            message = QMessageBox.warning(self, "Warning!", "Please select the database path!")

    @pyqtSlot()
    def on_RecogButton_clicked(self):
        if self._ui.DBtext.toPlainText() != "":
            self._ui.stackedWidget.setCurrentIndex(3)
            self._ui.RecogWidget.setCurrentIndex(0)
            self._ui.RecogStartButton.setText("Recognition")
            self._ui.RecogName_label.setText("")
            self.recognize_widget = RecogWidget(self)
        else:
            message = QMessageBox.warning(self, "Warning!", "Please select the database path!")

    def close(self):
        self.db_process.conn_db.close()
        self.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())