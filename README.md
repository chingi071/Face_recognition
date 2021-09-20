# Face_recognition

人臉辨識的實作過程分為幾個階段:

Face Detection: 使用 RetinaFace

Face Align

Feature extraction

Create Database: 使用 SQLite

Face Recognition: 使用 arcface

## 辨識結果:
    $ python recognize.py

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/result.jpg)

## 確認是否寫入資料庫裡
    $ python db_test.py

詳細流程可以參考我的 Medium: [Face Recognition 人臉辨識 Python 教學](https://medium.com/ching-i/face-recognition-%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-python-%E6%95%99%E5%AD%B8-75a5e2ef534f)