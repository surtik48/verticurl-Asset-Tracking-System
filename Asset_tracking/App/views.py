from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import logout
from datetime import date, datetime,timedelta
from django.forms.models import model_to_dict

import random
import smtplib, ssl
from email.message import EmailMessage


def Login(request):
    return render(request, 'App/Login.html')

def Admin_Dashboard(request):
    return render(request, 'App/Admin/Dashboard/Admin_Dashboard.html')

def newEmployee(request):
    return render(request, 'App/Admin/Employee/newEmployee.html')

def editEmployee(request):
    return render(request, 'App/Admin/Employee/editEmployee.html')

def newSupplier(request):
    return render(request, 'App/Admin/Supplier/newSupplier.html')

def editSupplier(request):
    return render(request, 'App/Admin/Supplier/editSupplier.html')

def newStock(request):
    return render(request, 'App/Admin/Stock/newStock.html')

def editStock(request):
    return render(request, 'App/Admin/Stock/editStock.html')

def newScrap(request):
    return render(request, 'App/Admin/Stock/Scrap/newScrap.html')

def editScrap(request):
    return render(request, 'App/Admin/Stock/Scrap/editScrap.html')

def newService(request):
    return render(request, 'App/Admin/Stock/newService.html')

def newWarranty(request):
    return render(request, 'App/Admin/Stock/newWarranty.html')

def allocationApproval(request):
    return render(request, 'App/Admin/Approval/allocationApproval.html')

def depreciationApproval(request):
    return render(request, 'App/Admin/Approval/depreciationApproval.html')

def inventoryVsAsset(request):
    return render(request, 'App/Admin/Chart/inventoryVsAsset.html')

def demo(request):
    return render(request, 'App/Admin/demo.html')

def stock(request):
    return render(request, 'App/Admin/Dashboard/stock.html')

def editDepreciation(request):
    return render(request, 'App/Admin/Stock/editDepreciation.html')

def viewStock(request):
    return render(request, 'App/Admin/Stock/viewStock.html')

def employee(request):
    return render(request, 'App/Admin/Dashboard/employee.html')

def supplier(request):
    return render(request, 'App/Admin/Dashboard/supplier.html')

def viewEmployee(request):
    return render(request, 'App/Admin/Employee/viewEmployee.html')

def viewSupplier(request):
    return render(request, 'App/Admin/Supplier/viewSupplier.html')

def scanQR(request):
    return render(request, 'QR/scanQR.html')

def createQR(request):
    return render(request, 'QR/createQR.html')
