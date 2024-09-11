import mysql.connector 


connection=mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='root'
)
if connection.is_connected():
    print("succesfully connected to the database")


    cursor = connection.cursor()
    create_table_query ="""
        CREATE TABLE IF NOT EXISTS STUDENTS(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT,
        gender VARCHAR(10)
        )
        """
    cursor.execute(create_table_query)
    print("table 'students' created succesfully.")


    insert_query = """
              INSERT INTO students(name, age, gender)
              VALUES(%s, %s, %s)
              """
    student_records=[
            ('alice',22,'female'),
            ('bob',24,'male'),
            ('charlie',25,'male')
            ]
    cursor.executemany(insert_query, student_records)
    connection.commit()
    print(f"{cursor.rowcount}records insrted into 'students' table.")

    select_query = "SELECT * FROM students"
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("Fetching data from 'students' table:")
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")
