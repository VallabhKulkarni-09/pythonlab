import sqlite3

def create_database_table():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS example_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')

    cursor.executemany('INSERT INTO example_table (name, age) VALUES (?, ?)',
                       [('John', 25), ('Alice', 30), ('Bob', 22)])

    connection.commit()
    connection.close()

def modify_table_data():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    print("Current data in the table:")
    cursor.execute('SELECT * FROM example_table')
    for row in cursor.fetchall():
        print(row)

    new_age = 28
    modified_name = 'John'
    cursor.execute('UPDATE example_table SET age = ? WHERE name = ?', (new_age, modified_name))

    print("\nModified data in the table:")
    cursor.execute('SELECT * FROM example_table')
    for row in cursor.fetchall():
        print(row)

    connection.commit()
    connection.close()

create_database_table()
modify_table_data()
