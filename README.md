# Face Recognition

人臉辨識的實作過程分為幾個階段:

Face Detection: 使用 RetinaFace

Face Align

Feature extraction

Create Database: 使用 SQLite

Face Recognition: 使用 arcface

## Project
將 Face Recognition 整合至專案，功能有: 設置資料庫、新增個人資料、辨識人臉

    $ python main.py

主畫面如下

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/Image%201.png)

### 設置資料庫畫面

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/Image%202.png)

### 新增個人資料分為拍照及從電腦選取照片

- 使用拍照功能

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/Image%203.png)

- 從電腦選取照片

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/Image%204.png)

### 辨識人臉

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/Image%205.png)


## 執行單一照片辨識:
    $ python recognize.py

![image](https://github.com/chingi071/Face_recognition/blob/main/README_pix/result.jpg)

## 確認是否寫入資料庫裡
    $ python db_test.py

詳細流程可以參考我的 Medium: [Face Recognition 人臉辨識 Python 教學](https://medium.com/ching-i/face-recognition-%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-python-%E6%95%99%E5%AD%B8-75a5e2ef534f)