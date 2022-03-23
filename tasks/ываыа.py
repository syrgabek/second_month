import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()
    except Error as e:
        print(e)


def insert_student(conn, student):
    try:
        sql = '''INSERT INTO students (full_name, mark, hobby, birth_date, is_married) 
        VALUES (?, ?, ?, ?, ?);'''
        c = conn.cursor()
        c.execute(sql, student)
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def update_student_mark(conn, mark, id):
    try:
        sql = '''update students set mark = ? where id = ?;'''
        c = conn.cursor()
        c.execute(sql, (mark, id))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def delete_student(conn, id):
    try:
        sql = '''delete from students where id = ?;'''
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def select_all_students(conn):
    try:
        sql = '''select * from students;'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def select_all_students_whose_mark_bigger_than(conn, mark):
    try:
        sql = '''select full_name, mark from students where mark >= ?;'''
        c = conn.cursor()
        c.execute(sql, (mark,))
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


database = r'group15.db'
conn = create_connection(database)
sql_create_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL,
mark DOUBLE(5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN NOT NULL DEFAULT false
);
'''

if conn is not None:
    print('Successfully connected')

    # create_table(conn, sql_create_students_table)
    # insert_student(conn, ('Amantur Bakytov', 97.9, None, '1998-06-11', False))
    # insert_student(conn, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    # insert_student(conn, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    # insert_student(conn, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    # insert_student(conn, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    # insert_student(conn, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    # insert_student(conn, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    # insert_student(conn, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    # insert_student(conn, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    # insert_student(conn, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    # insert_student(conn, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    # insert_student(conn, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    # insert_student(conn, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))

    # update_student_mark(conn, 60.5, 2)
    # delete_student(conn, 2)
    # select_all_students(conn)
    select_all_students_whose_mark_bigger_than(conn, 50.0)

    conn.close()