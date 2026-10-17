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