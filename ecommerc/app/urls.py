
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    path('furits',views.Fruits, name ='furits'),
    path('services', views.Services, name='services'),
    path('contact',views.Contact, name='contact'),
    path('details', views.Details, name='details'),
    path('buy/<int:pk>/',views.BuyProduct, name='buy'),
    path('add',views.Add_to_cart, name='add'),
    path('payment', views.PayMent, name='payment'),
    path('order',views.Orders, name='order'),
    path('show', views.show_cart, name = 'show'),
    path('delete<int:pk>',views.Delete,name ='delete'),
    path('update', views.Update, name='update'),
]
