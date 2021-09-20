import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtMultimedia
import numpy as np
import time

class RecogWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self._ui = self._parent._ui
        self.recognize_process = self._parent.recognize_process

        camera_device = QByteArray()
        self.set_camera(camera_device)

        self._ui.RecogBackButton.clicked.connect(self.on_RecogBackButton_clicked)
        self._ui.RecogStartButton.clicked.connect(self.on_RecogStartButton_clicked)

    # =====================================================
    def set_camera(self, camera_device):
        if camera_device.isEmpty():
            self.camera = QtMultimedia.QCamera()
        else:
            self.camera = QtMultimedia.QCamera(camera_device)

        self.camera.error.connect(self.display_camera_error)

        self.camera.setViewfinder(self._ui.RecogView)
        self.camera.start()

    def display_camera_error(self):
        message = QMessageBox.warning(self, "Camera error", self.camera.errorString())

    # =====================================================
    def on_RecogStartButton_clicked(self):
        if self._ui.RecogStartButton.text() == "Recognition":
            self.imageCapture = QtMultimedia.QCameraImageCapture(self.camera)
            self.imageCapture.imageCaptured.connect(self.process_CapturedImage)

            detect_dir_path = 'detect'
            if not os.path.exists(detect_dir_path):
                os.mkdir(detect_dir_path)

            timestamp = time.time()
            detect_pix_path = os.path.join(os.getcwd(), detect_dir_path, str(timestamp)+ '.jpg')
            self.imageCapture.capture(detect_pix_path)

            self._ui.RecogStartButton.setText("Again")

        else:
            self._ui.RecogWidget.setCurrentIndex(0)
            self._ui.RecogStartButton.setText("Recognition")
            self._ui.RecogName_label.setText("")

    def process_CapturedImage(self, requestId, img):
        self._ui.RecogWidget.setCurrentIndex(1)
        scaled_image = img.scaled(self._ui.RecogView.size(), 1, 1)

        pixmap_camera = QPixmap.fromImage(scaled_image)
        self._ui.RecogImage.setPixmap(pixmap_camera)
        mat_image = self.image_to_mat(scaled_image)

        self.compare_face(mat_image)

    def image_to_mat(self, img):
        ptr = img.constBits()
        ptr.setsize(img.byteCount())
        mat = np.array(ptr).reshape(img.height(), img.width(), 4)

        return mat

    # =====================================================
    def compare_face(self, mat_image):
        self.db_process = self._parent.db_widget.db_process
        db_data = self.db_process.get_face_info()

        if db_data != []:
            final_embedding = self.recognize_process.get_final_embedding(mat_image)

            total_db_data = []
            for data in db_data:
                person_info = []

                person_name = data[1]
                person_embeddings = self.db_process.convert_array(data[2])

                person_info.append(person_name)
                person_info.append(person_embeddings)
                total_db_data.append(person_info)

            name, distance, total_result = self.recognize_process.compare_face(total_db_data, final_embedding)
            RecogName_text = "Hello! " + name
            self._ui.RecogName_label.setText(RecogName_text)

        else:
            message = QMessageBox.warning(self, "Warning!", "Please create personal information!")

    # =====================================================
    def on_RecogBackButton_clicked(self):
        self.camera.stop()
        self._ui.stackedWidget.setCurrentIndex(0)

    # =====================================================
    def closeEvent(self, event):
        self.camera.stop()