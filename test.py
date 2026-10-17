import pymysql

# 第一步：通过pymysql的connect函数，获取连接对象
"""
    connect函数：
        作用：通过数据库的连接信息，返回一个数据库连接对象
        参数：
            1.host：连接数据库服务器所在的ip地址：127.0.0.1
            2.port：连接数据库服务器的端口号：3306
            3.user：连接数据库服务器的账号,root
            4.password:连接数据库服务器账号对应的密码
            5.database：连接数据库服务器之后想要操作的数据库的名字
            6.charser：字符集,utf8
"""
conn=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='yolo',
    charset='utf8'
)

# 第二步：通过连接对象调用方法cursor()，得到一个游标对象
cur=conn.cursor()

# 第三步:定义操作数据库的sql语句
sql="select * from `users`;"

# 第四步：通过游标对象调用方法execute(参数1,参数2)执行sql语句
"""
    execute方法：
        作用：非批量操作，执行一条sql语句，返回值是影响数据的行数
        参数：
            1.sql语句
            2.【可选】为sql语句中的占位符赋值，赋值的数据类型必须是字典/元组/列表
"""
rows=cur.execute(sql)
print(rows)

# 第五步：通过游标对象.fetchall()方法获取查询结果
result=cur.fetchall()
print("查询结果：",result)

# 第六步：关闭连接
cur.close()
conn.close()