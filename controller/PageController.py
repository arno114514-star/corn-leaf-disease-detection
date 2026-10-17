#
from django.shortcuts import render

#
def go_a(request):
    print("进入了go_a函数")
    # 从GET请求参数中获取username和age参数
    username = request.GET.get("username")
    age = request.GET.get("age")
    """
        render函数常用参数:
            1.request:函数的形式参数
            2.template_name:访问的页面，以templates为起点
            3.context：返回给页面的数据，以键值对格式，页面可通过{{key}}取出对应的value
            4.content_type:如果需要返回数据给页面的时候，以什么格式返回
    """
    # 将获取到的参数传递给模版
    context = {"username":username,"age":age}
    return render(request,"a.html",context)

def go_login(request):
    return render(request,"login.html")

def go_system(request):
    return render(request,"system.html")

def go_imDetect(request):
    return render(request,"imgDetect.html")