from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('addcat/',views.addcat,name='addcat'),
    path('getcat/',views.getcat,name='getcat'),
    path('addprd/',views.addprd,name='addprd'),
    path('getprd/',views.getprd,name='getprd'),
    path('viewcat/',views.viewcat,name='viewcat'),
    path('viewprd/',views.viewprd,name='viewprd'),
    path('editcat/<int:id>/',views.editcat,name='editcat'),
    path('updatecat/<int:id>/',views.updatecat,name='updatecat'),
    path('deletecat/<int:id>/',views.deletecat,name='deletecat'),
    path('editprd/<int:id>/',views.editprd,name='editprd'),
    path('updateprd/<int:id>/',views.updateprd,name='updateprd'),
    path('deleteprd/<int:id>/',views.deleteprd,name='deleteprd'),
    path('viewcon/',views.viewcon,name='viewcon'),
    path('usrcheckout/',views.usrcheckout,name='usrcheckout')

]
