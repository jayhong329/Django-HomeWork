from django.shortcuts import render, redirect
from .models import Djangohw
from datetime import datetime

# Create your views here.
def index(request):

    # 資料庫的操作
    # 讀取所有會員資料
    alltodo = Djangohw.objects.all()

    # 資料新增
    # 接收使用者上傳的資料
    if request.method == "POST":
        completed = request.POST.get("completed")
        learnsomething = request.POST.get("todo")
        last_update = request.POST.get("last_update")

    # 將表單傳過來的資料寫進資料庫
        Djangohw.objects.create(
            completed = completed, 
            todo = learnsomething,
            last_update = last_update
        )
    return render(request, 'djangoHW/index.html', {"alltodo":alltodo})



    # 刪除資料
def delete(request, id): 
    # 1. 先找到要修改的資料
    todo = Djangohw.objects.get(todo_id=id )
    # 2.進行刪除
    todo.delete()
    return redirect('djangoHW:index')