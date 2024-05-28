from django.urls import path
from .import views
urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('singleprd/<int:id>/',views.singleprd,name='singleprd'),
    path('product/<str:category>/',views.product,name='product'),
    path('reg/',views.reg,name='reg'),
    path('getreg/',views.getreg,name='getreg'),
    path('login/',views.login,name='login'),
    path('getlog/',views.getlog,name='getlog'),
    path('contact/',views.contact,name='contact'),
    path('getct/',views.getct,name='getct'),
    path('logout/',views.logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('cartdata/<int:id>/',views.cartdata,name='cartdata'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkoutdata/',views.checkoutdata,name='checkoutdata')
]