import mysql.connector as mysql


def initDB():
    db = mysql.connect(
        host = "localhost",
        user = "your_login",
        passwd = "your_password",
        database = "your_db_name"
    )

    return db

