import os
import sqlite3
import io
import numpy as np

class DBProcess():
    def __init__(self, db_sql_path):
        sqlite3.register_adapter(np.ndarray, self.adapt_array)
        sqlite3.register_converter("ARRAY", self.convert_array)

        if not os.path.exists(db_sql_path):
            self.conn_db = sqlite3.connect(db_sql_path)
            self.conn_db.execute("CREATE TABLE face_info \
                                     (id INT PRIMARY KEY NOT NULL, \
                                     name TEXT NOT NULL, \
                                     embedding ARRAY NOT NULL)")

            self.conn_db.commit()

        else:
            self.conn_db = sqlite3.connect(db_sql_path)

    def set_face_info(self, person_id, person_name, adapt_embedding):
        self.conn_db.execute("INSERT INTO face_info (id, name, embedding) VALUES (?, ?, ?)",
                        (person_id, person_name, adapt_embedding))
        self.conn_db.commit()

    def get_face_info(self):
        cursor = self.conn_db.execute("SELECT * FROM face_info")
        db_data = cursor.fetchall()

        return db_data

    def get_face_info_id(self):
        cursor = self.conn_db.execute("SELECT id FROM face_info")
        total_face_id = [face_id for face_id in cursor]

        return total_face_id

    def get_last_face_id(self):
        total_face_id = self.get_face_info_id()

        if total_face_id == []:
            face_info_id = -1

        else:
            face_info_id = np.max(total_face_id)

        return face_info_id

    def get_person_face_id(self, person_name):
        cursor = self.conn_db.execute("SELECT id FROM face_info WHERE name=?", (person_name,))
        db_data = cursor.fetchall()

        return db_data

    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)