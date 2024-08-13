from django.shortcuts import render, redirect
from .models import Djangohw

# Create your views here.
def index(request):

    # 資料庫的操作
    # 讀取所有會員資料
    alltodo = Djangohw.objects.all()
    # djangohw = Djangohw.objects.get(todolist=2)
    print(alltodo)

    return render(request, 'djangoHW/index.html', {"alltodo":alltodo} )
    # 資料新增
    # Member.objects.create(
    #     member_name = "qweasd",
    #     member_password = "123456",
    #     member_birth = "2028-04-28",
    #     member_email = "qweasd@gmail.com"
    # )

    # 刪除資料
    # 1. 先找到要修改的資料
    # member = Member.objects.get(member_id=5)
    # 2.進行刪除
    # member.delete()
    # return HttpResponse("資料庫操作練習")


# def delete(request, id): 
#     member = Djangohw.objects.get(todolist=id)
#     member.delete()
#     return redirect('djangoHW:index')