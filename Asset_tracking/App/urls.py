from django.contrib.admin.decorators import register
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path('Login/',views.Login,name='Login'),
    path('Admin_Dashboard/',views.Admin_Dashboard,name='Admin_Dashboard'),
    path('newEmployee/',views.newEmployee,name='newEmployee'),
    path('editEmployee/',views.editEmployee,name='editEmployee'),
    path('newSupplier/',views.newSupplier,name='newSupplier'),
    path('editSupplier/',views.editSupplier,name='editSupplier'),
    path('newStock/', views.newStock, name='newStock'),
    path('editStock/', views.editStock, name='editStock'),
    path('newScrap/', views.newScrap, name='newScrap'),
    path('editScrap/', views.editScrap, name='editScrap'),
    path('newService/', views.newService, name='newService'),
    path('newWarranty/', views.newWarranty, name='newWarranty'),
    path('allocationApproval/', views.allocationApproval, name='allocationApproval'),
    path('depreciationApproval/', views.depreciationApproval, name='depreciationApproval'),
    path('inventoryVsAsset/', views.inventoryVsAsset, name='inventoryVsAsset'),
    path('editDepreciation/', views.editDepreciation, name='editDepreciation'),
    path('demo/', views.demo, name='demo'),
    path('stock/', views.stock, name='stock'),
    path('viewStock/', views.viewStock, name='viewStock'),
    path('employee/', views.employee, name='employee'),
    path('viewEmployee/', views.viewEmployee, name='viewEmployee'),
    path('supplier/', views.supplier, name='supplier'),
    path('viewSupplier/', views.viewSupplier, name='viewSupplier'),
    path('scanQR/', views.scanQR, name='scanQR'),

]

