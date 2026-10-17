from django.http import JsonResponse
from service import UserService
from service import DetectService

def login(request):
    print("准备验证账号和密码")
    username = request.GET.get("username")
    password = request.GET.get("password")
    print("用户名：",username)
    print("密码",password)
    return JsonResponse(UserService.login(username,password))

def img_detect(request):
    """
       Django
    """
    file = request.FILES.get("file")
    return JsonResponse(DetectService.img_detect(file))