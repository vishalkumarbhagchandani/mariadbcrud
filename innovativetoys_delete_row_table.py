import mariadb
import sys
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="innovativetoys"
    )
    cur=conn.cursor() #cursor is an object that will execute the SQL statements and stores the output
    #print("inside try") 
    cur.execute("delete from Customer where customer_id=1215")
    cur.execute("select * from Customer")
    for row_in_table in cur:
        print(row_in_table);
    conn.commit()
    conn.close()
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")  #f is for formating and here we are printing the error if connection is not success
    sys.exit(1)

