from datetime import datetime
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin,User,SL_Master,SL_DEVICE_LIST,LAB
from django.contrib import messages
# Create your views here.
import json
import pytz


# from django.contrib.auth import login as auth_login
# from django.shortcuts import render, redirect


def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def login(request):
    print("123")
    if request.method == "POST":
        U_name = request.POST['Unm']
        print("U_name",U_name)
        A_Pwd = request.POST['pwd']
        print("A_Pwd",A_Pwd)
        try:
            admin = Admin.objects.get(username = U_name).__dict__
            print("111", admin)
            name = admin.get('username')
            pwd2 = admin.get('password')
        except:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
        if(U_name==name and A_Pwd==pwd2): 
            messages.success(request,'Logged in successfully')
            lab_objs = LAB.objects.all()
            return render(request,"show.html", {'lab_obj':lab_objs})
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
       
def Register(request):
    return render(request,'register.html')

def LAB_view(request):
    # device_list = SL_DEVICE_LIST.objects.get(PRODUCT_ID_id = pk).__dict__
    # lab_objs = LAB.objects.get(LAB_ID =device_list['LAB_ID_id'])
    print(" XXXXXXXXXXXXXXXXXXX ")
    lab_objs = LAB.objects.all()
    return render(request,'show.html',{'lab_obj':lab_objs})

def device_view(request,pk):
    device_list = SL_DEVICE_LIST.objects.filter(LAB_ID_id = pk)
    # lab_objs = LAB.objects.filter(LAB_ID =device_list['LAB_ID_id'])
    # device_list =SL_DEVICE_LIST.objects.all()
    return render(request,'device_list.html',{'device_obj':device_list})

def allocation_view(request,pk):
    lab_objs = LAB.objects.filter(ID = pk)
    print("allocation_view  xyz")
    # lab_objs = LAB.objects.filter(LAB_ID =device_list['LAB_ID_id'])
    # device_list =SL_DEVICE_LIST.objects.all()
    return render(request,'allocation.html')

def tobeadded(request):
    print("tobeadded xyz")

    sDate = request.POST['sDate']
    print("sDate :: ",sDate)
    eDate = request.POST['eDate']
    print("eDate :: ",eDate)

    lab_objs = LAB.objects.filter(ID=1)
    row = lab_objs[0]

    print(row.available_end_date)
    avEDate = row.available_end_date


    e1Date = eDate.replace("-", "/")
    e1s = datetime.strptime(e1Date, "%Y/%m/%d")
    print(" --- ",avEDate.date)

    diff = datetime.datetime.now(avEDate)

    epoch = datetime.datetime.utcfromtimestamp(avEDate)
    print(" ii ",epoch)




 
    





    # available_start_date = lab_objs.get('DUT_ID')
    # available_end_date = lab_objs.get('available_end_date')


    # print("available_start_date ::"+available_start_date)
    # print("available_end_date ::"+available_end_date)


    return render(request,'tobeadded.html')
