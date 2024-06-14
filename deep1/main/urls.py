from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('payment-delivery/', views.payment_delivery, name='payment-delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('work-group/', views.work_group, name='work-group'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
