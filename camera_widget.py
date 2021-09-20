import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtMultimedia

class CameraWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self._ui = self._parent._ui
        self.recognize_process = self._parent.recognize_process
        self.db_process = self._parent.db_widget.db_process

        self.camera_device = QByteArray()
        self.set_camera(self.camera_device)

        self.choose_pix_path = ""
        self._ui.NameWarn.setText("")
        self._ui.Nametext.setPlainText("")

        self._ui.CaptureButton.clicked.connect(self.on_CaptureButton_clicked)
        self._ui.ChooseButton.clicked.connect(self.on_ChooseButton_clicked)
        self._ui.SaveButton.clicked.connect(self.on_SaveButton_clicked)
        self._ui.BackButton.clicked.connect(self.on_BackButton_clicked)

    def set_camera(self, camera_device):
        if camera_device.isEmpty():
            self.camera = QtMultimedia.QCamera()
        else:
            self.camera = QtMultimedia.QCamera(camera_device)

        self.camera.error.connect(self.display_camera_error)

        self.camera.setViewfinder(self._ui.CameraView)
        self.camera.start()

    def display_camera_error(self):
        message = QMessageBox.warning(self, "Camera error", self.camera.errorString())

    # =====================================================
    # Photo
    def on_CaptureButton_clicked(self):
        bool_fill = self.check_fill_in_name()
        if bool_fill:
            self.process_CaptureButton()

    def process_CaptureButton(self):
        if self._ui.CaptureButton.text() == "Take a picture":
            self.imageCapture = QtMultimedia.QCameraImageCapture(self.camera)
            self.imageCapture.imageCaptured.connect(self.process_CapturedImage)
            self.imageCapture.capture()

            self._ui.CaptureButton.setText("Take another picture")

        else:    # self._ui.CaptureButton.text() == "Take another picture"
            self._ui.CameraWidget.setCurrentIndex(0)
            self._ui.CaptureButton.setText("Take a picture")

    def process_CapturedImage(self, requestId, img):
        self._ui.CameraWidget.setCurrentIndex(1)
        scaled_image = img.scaled(self._ui.CameraView.size(), 1, 1)
        self._ui.CapturedImage.setPixmap(QPixmap.fromImage(scaled_image))

    # =====================================================
    # Load
    def on_ChooseButton_clicked(self):
        FileName_path, _ = QFileDialog.getOpenFileName(self, "Choose a picture", "./")
        if FileName_path:
            self.choose_pix_path = FileName_path
            choose_pix = QPixmap(self.choose_pix_path)
            self._ui.CameraWidget.setCurrentIndex(2)
            self._ui.ChooseImage.setGeometry(QRect(220, 20, 541, 411))
            self.set_resize_pix(choose_pix, self._ui.ChooseImage)
            self._ui.CaptureButton.setText("Save picture")

    def set_resize_pix(self, pix, label):
        label_w = label.width()
        label_h = label.height()
        width, height = self.pix_resize(pix, label_w, label_h)
        label.setPixmap(pix)
        label.resize(width, height)
        label.setScaledContents(True)

    def pix_resize(self, pix, label_w, label_h):
        pix_w = pix.width()
        pix_h = pix.height()

        f1 = label_w / pix_w
        f2 = label_h / pix_h
        factor = min([f1, f2])
        width = int(pix_w * factor)
        height = int(pix_h * factor)

        return width, height

    # =====================================================
    def on_SaveButton_clicked(self):
        bool_fill = self.check_fill_in_name()

        if bool_fill:
            ui_label = self.process_mode_case()
            bool_duplicate_name = self.check_duplicate_person_name()

            if ui_label != "" and not bool_duplicate_name:
                person_name = self._ui.Nametext.toPlainText()

                person_pix_path = self.get_person_pix_path()
                self.process_SaveButton(ui_label, person_pix_path)
                self.set_db_face_info(person_name, person_pix_path)

    def process_mode_case(self):
        mode_photo = self._ui.ButtonWidget.currentIndex() == 0
        mode_load = self._ui.ButtonWidget.currentIndex() == 1
        bool_click = self._ui.CameraWidget.currentIndex() == 1
        ui_label = ""

        if mode_photo:
            if bool_click:
                ui_label = self._ui.CapturedImage

            else:
                message = QMessageBox.warning(self, "Warning!", "Please take a picture!")

        elif mode_load:
            if self.choose_pix_path:
                ui_label = self._ui.ChooseImage

            else:
                message = QMessageBox.warning(self, "Warning!", "Please choose a picture!")

        else:
            pass

        return ui_label

    # =====================================================
    def get_person_pix_path(self):
        person_name = self._ui.Nametext.toPlainText()
        db_file_path = self._ui.DBtext.toPlainText()
        person_file = os.path.join(db_file_path, person_name)

        if not os.path.exists(person_file):
            os.mkdir(person_file)

        person_pix_path = os.path.join(person_file, person_name + '.jpg')

        return person_pix_path

    def process_SaveButton(self, ui_label, person_pix_path):
        ui_label.pixmap().save(person_pix_path)

    def set_db_face_info(self, person_name, img_path):
        final_embedding = self.recognize_process.get_final_embedding(img_path)
        adapt_embedding = self.db_process.adapt_array(final_embedding)

        face_info_id = self.db_process.get_last_face_id()
        person_id = face_info_id + 1
        self.db_process.set_face_info(str(person_id), person_name, adapt_embedding)

        message = QMessageBox.information(self, "Information", "The picture has been saved to the database!")

    # =====================================================
    def check_fill_in_name(self):
        if self._ui.Nametext.toPlainText() == "":
            self._ui.NameWarn.setText("Please fill in!")
            self._ui.NameWarn.setStyleSheet('color: rgb(255, 0, 0);')
            message = QMessageBox.warning(self, "Warning!", "Please fill in your name!")
            return 0

        else:
            self._ui.NameWarn.setText("")
            return 1

    def check_duplicate_person_name(self):
        person_name = self._ui.Nametext.toPlainText()
        db_data = self.db_process.get_person_face_id(person_name)

        if db_data != []:
            message = QMessageBox.warning(self, "Warning!", "The person’s picture is already stored in the database!")

            return 1

        else:
            return 0

    # =====================================================
    def on_BackButton_clicked(self):
        self.camera.stop()
        self._ui.stackedWidget.setCurrentIndex(0)

    # =====================================================
    def closeEvent(self, event):
        self.camera.stop()


