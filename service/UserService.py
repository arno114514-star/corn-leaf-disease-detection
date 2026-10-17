# login函数处理逻辑代码--返回值是一个字典
"""
    service中的返回字典，按照以下格式定义
    {
        status:int类型，状态码，200成功，500失败
        msg:字符串，提示信息
        data:任意类型，返回值是数据
    }
"""
from util import MySQLUtil

def login(username,password):
    """
        验证流程：
            1.验证账号，账号验证不通过，返回账号不存在
            2.账号验证通过，验证密码，密码验证不通过，返回密码错误
            3.返回登录成功
    """
    conn=MySQLUtil.connect()
    cur=conn.cursor()
    sql="select * from `users` where username=%s;"
    cur.execute(sql,(username,))
    result=cur.fetchone()
    print(result)
    # 根据result的结果判断，如果result结果是none，那么账号不存在
    if result==None:
        MySQLUtil.close(conn,cur)
        return{
            'status':500,
            "msg":"账号不存在"
        }
    else:
        # 账号存在，验证密码
        if result[1]==password:
            # 密码正确
            MySQLUtil.close(conn,cur)
            return{
                'status':200,
                "msg":"登录成功"
            }
        else:
            MySQLUtil.close(conn,cur)
            return{
                'status':500,
                "msg":"密码错误，登录失败"
            }

def register(username,password):
    """
        注册流程：
            1.校验用户名和密码非空
            2.查询用户名是否已存在，已存在则返回注册失败
            3.不存在则插入新用户，返回注册成功
    """
    # 简单的非空校验
    if username is None or username=="" or password is None or password=="":
        return{
            'status':500,
            "msg":"用户名或密码不能为空"
        }
    conn=MySQLUtil.connect()
    cur=conn.cursor()
    # 先查用户名是否已存在
    sql="select * from `users` where username=%s;"
    cur.execute(sql,(username,))
    result=cur.fetchone()
    if result is not None:
        MySQLUtil.close(conn,cur)
        return{
            'status':500,
            "msg":"用户名已存在"
        }
    # 插入新用户
    sql="insert into `users`(username,password) values(%s,%s);"
    cur.execute(sql,(username,password))
    conn.commit()
    MySQLUtil.close(conn,cur)
    return{
        'status':200,
        "msg":"注册成功"
    }