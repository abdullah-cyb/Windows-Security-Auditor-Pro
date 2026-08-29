# database.py

import sqlite3
from datetime import datetime


DATABASE_NAME = "security_audit.db"



class Database:


    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE_NAME
        )

        self.create_table()



    def create_table(self):

        cursor = self.connection.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            score INTEGER,

            level TEXT,

            details TEXT

        )
        """)


        self.connection.commit()



    def save_scan(
            self,
            score,
            level,
            details
        ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO scans
            (
                date,
                score,
                level,
                details
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?
            )
            """,

            (
                str(datetime.now()),
                score,
                level,
                details
            )

        )


        self.connection.commit()



    def get_history(self):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            SELECT *
            FROM scans
            ORDER BY id DESC
            """
        )


        return cursor.fetchall()



    def delete_all(self):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            DELETE FROM scans
            """
        )


        self.connection.commit()



    def close(self):

        self.connection.close()



# اختبار الملف

if __name__ == "__main__":


    db = Database()


    db.save_scan(
        85,
        "Good",
        "Firewall Enabled"
    )


    history = db.get_history()


    for row in history:
        print(row)


    db.close()