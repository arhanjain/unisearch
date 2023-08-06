import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="unisearch_db"
        )

cursor = db.cursor()

cursor.execute("CREATE TABLE Papers (title VARCHAR(200), url VARCHAR(2048), paperID int PRIMARY KEY AUTO_INCREMENT)")


