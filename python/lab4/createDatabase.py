import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'zzy123456',
    'database': 'mqtt'
}


def create_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mqtt")
    cursor.execute("USE mqtt")
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP, sensor_type VARCHAR(255), value FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS sent_alerts (id INT AUTO_INCREMENT PRIMARY KEY, sensor_type VARCHAR(255), value FLOAT, timestamp TIMESTAMP)")
    conn.close()

def main():
    create_database()

if __name__ == '__main__':
    main()