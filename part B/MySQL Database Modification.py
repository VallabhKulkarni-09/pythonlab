import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="studentdb")
cur = mydb.cursor()

try:
    cur.execute("CREATE TABLE emp1(name VARCHAR(200), desig VARCHAR(20), sal INT(20))")

    query = "INSERT INTO emp1(name, desig, sal) VALUES (%s, %s, %s)"
    val = [("bahubali", "manager", 30000), ("parv", "CEO", 50000)]
    cur.executemany(query, val)

    cur.execute("SELECT * FROM emp1")
    resultdb = cur.fetchall()
    for row in resultdb:
        print(row)

    query1 = "UPDATE emp1 SET sal = 70000 WHERE name = 'bahubali'"
    cur.execute(query1)

    cur.execute("SELECT * FROM emp1")
    result = cur.fetchall()

    for r in result:
        print(r)

    mydb.commit()

except Exception as e:
    print("Error:", e)
    mydb.rollback()

mydb.close()
