import mysql.connector as sql
try:
    db=sql.connect(
        host = "localhost",
        user = 'root',
        password = "",
        database = "moayed"
    )
    
    cr=db.cursor()
    cr.execute("CREATE DATABASE if not exists moayed")
    cr.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) UNIQUE, email VARCHAR(50) UNIQUE, password VARCHAR(100))")
    cr.execute("INSERT INTO users(username, email, password) Values(%s, %s, %s)",("moayed", "qwermoaid17@gmail.com", "moiadQWER-92"))
    db.commit()

except sql.Error as r:
    print(r)