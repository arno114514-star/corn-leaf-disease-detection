import pymysql

def connect():
    return pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='yolo',
    charset='utf8'
)

def close(conn,cur):
    conn.close()
    cur.close()