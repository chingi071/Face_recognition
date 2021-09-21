import os
import cv2
import numpy as np
from skimage import transform as trans
import onnxruntime as rt
from retinaface import RetinaFace
from sklearn.preprocessing import normalize

class RecogProcess():
    def __init__(self):
        self.detector = RetinaFace(quality="normal")
        onnx_path = "model/arcface_r100_v1.onnx"
        self.extractor = rt.InferenceSession(onnx_path)
        self.threshold = 1

    def compare_face(self, total_db_data, final_embedding):
        total_names = []
        total_distances = []
        for i in range(len(total_db_data)):
            person_name = total_db_data[i][0]
            total_names.append(person_name)

            person_embeddings = total_db_data[i][1]
            distance = round(np.linalg.norm(person_embeddings - final_embedding), 2)
            total_distances.append(distance)

        total_result = dict(zip(total_names, total_distances))
        idx_min = np.argmin(total_distances)
        distance, name = total_distances[idx_min], total_names[idx_min]

        if distance < self.threshold:
            return name, distance, total_result
        else:
            name = "Unknown Person"
            return name, distance, total_result

    def get_final_embedding(self, img_path):
        img_rgb, detections = self.face_detect(img_path)
        position, landmarks, embeddings = self.get_embeddings(img_rgb, detections)

        return embeddings

    def face_detect(self, img_path):
        if isinstance(img_path, str):
            img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
            img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        else:  # np.ndarray
            img_rgb = cv2.cvtColor(img_path, cv2.COLOR_BGR2RGB)

        detections = self.detector.predict(img_rgb)

        return img_rgb, detections

    def face_align(self, img_rgb, landmarks):
        src = np.array([
            [30.2946, 51.6963],
            [65.5318, 51.5014],
            [48.0252, 71.7366],
            [33.5493, 92.3655],
            [62.7299, 92.2041]], dtype=np.float32)
        dst = np.array(landmarks, dtype=np.float32).reshape(5, 2)
        tform = trans.SimilarityTransform()
        tform.estimate(dst, src)
        M = tform.params[0:2, :]
        aligned = cv2.warpAffine(img_rgb, M, (112, 112), borderValue=0)

        return aligned

    def get_embeddings(self, img_rgb, detections):
        position = []
        landmarks = []
        embeddings = np.zeros((len(detections), 512))
        for i, face_info in enumerate(detections):
            face_position = [face_info['x1'], face_info['y1'], face_info['x2'], face_info['y2']]
            face_landmarks = [face_info['left_eye'], face_info['right_eye'], face_info['nose'], face_info['left_lip'],
                              face_info['right_lip']]

            position.append(face_position)
            landmarks.append(face_landmarks)

            aligned = self.face_align(img_rgb, face_landmarks)
            t_aligned = np.transpose(aligned, (2, 0, 1))

            inputs = t_aligned.astype(np.float32)
            input_blob = np.expand_dims(inputs, axis=0)

            first_input_name = self.extractor.get_inputs()[0].name
            first_output_name = self.extractor.get_outputs()[0].name

            predict = self.extractor.run([first_output_name], {first_input_name: input_blob})[0]
            final_embedding = normalize(predict).flatten()

            embeddings[i] = final_embedding

        return position, landmarks, embeddings

