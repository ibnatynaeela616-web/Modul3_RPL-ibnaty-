#Ibnaty Naeela_F5212510008
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = "localhost"
        self.db_name = "perpustakaan"
        self.username = "root"
        self.password = ""  # Ubah jika MySQL Anda menggunakan password
        self.conn = None

    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.db_name,
                user=self.username,
                password=self.password
            )
            if self.conn.is_connected():
                return self.conn
        except Error as e:
            print(f"Koneksi Gagal: {e}")
            return None

        