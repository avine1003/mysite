from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.models import User


def index(request):
    data = [1,2,3,4]
    # return HttpResponse("hello world")
    return render(request, 'index.html', {'data': data})

def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    try:
        user = User.objects.get(username=username)
        if user:
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('帐号不存在')
    except:
        return HttpResponse('网络异常')


def register(request):
    # 获取客户端通过get发送来的数据
    username = request.GET.get('username')
    password = request.GET.get('password')

    result ='注册失败'

    try:
        user = User.objects.filter(username=username)
        if user:
            result = '用户已存在'
        else:
            User.objects.create(username=username, password=password)
            result = '注册成功'
    except:
        pass
    return HttpResponse(result)


def update(request):
    uid = request.GET.get('uid')
    password = request.GET.get('password')
    try:
        User.objects.filter(pk=uid).update(password=password)
    except:
        pass
    return HttpResponse('更新成功')


# User.objects.dates()