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
        learnsomething = request.POST.get("todo")

    # 將表單傳過來的資料寫進資料庫
        Djangohw.objects.create(
            todo = learnsomething,
        )
    return render(request, 'djangoHW/index.html', {"alltodo":alltodo})

    # 修改資料
def edit(request, id):
    # 1. 先找到要修改的資料
    djangohw = Djangohw.objects.get(todo_id=id)
    # 2.進行修改
    if request.method == "POST":
        completed_status = request.POST.get("completed") == "on"
        djangohw.completed = completed_status
        djangohw.save()
    return redirect('djangoHW:index')


    # 刪除資料
def delete(request, id): 
    # 1. 先找到要刪除的資料
    todo = Djangohw.objects.get(todo_id=id )
    # 2.進行刪除
    todo.delete()
    return redirect('djangoHW:index')