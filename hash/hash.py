import bcrypt
import pymysql

class App:
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host='localhost',
                user='kiselevW',
                password="kiselevW",
                database="project_managment_kiselev",
                port = 8889
            )
            cursor = self.db.cursor()
            sql = "Select password From logs"
            passwords_arr = []
            cursor.execute(sql)
            for itm in cursor.fetchall():
                passwords_arr+=itm
            for itm in passwords_arr:
                hashed_arr = []
            cursor.close()
            
                
            
        except pymysql.Error as e:
            print(f"err {e}")
            

if __name__ == "__main__":
    s = App()
