# convert all tables in database to utf8
import pymysql


db_mysql = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'autocommit': 'True'
}


connect_db = pymysql.connect(**db_mysql)
c_db = connect_db.cursor()

try:
    c_db.execute("show tables")
    row_tables=c_db.fetchall()
    for (table_name, ) in row_tables:
        c_db.execute("show columns from %s"%table_name)
	rows = c_db.fetchall()
        for row in rows:
	try:
	    c_db.execute("UPDATE %s SET %s = @txt where char_length(%s) = length(@txt :=  CONVERT(CAST(CONVERT(%s USING latin1) AS BINARY) USING utf8))"%(table_name, row[0], row[0], row[0]))
	except Exception as err:
	    print(err)

except Exception as e:
    print(e)

