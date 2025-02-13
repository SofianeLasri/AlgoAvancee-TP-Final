import mysql.connector

def verify_database_has_data(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tweets")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return len(result) > 0
    except mysql.connector.Error as e:
        print(e)
        return False