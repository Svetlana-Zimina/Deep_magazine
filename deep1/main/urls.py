from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'payment-delivery/',
        views.PaymentDeliveryView.as_view(),
        name='payment-delivery'
    ),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('work-group/', views.WorkGroupView.as_view(), name='work-group'),
    path(
        'privacy-policy/',
        views.PrivacyPolicyView.as_view(),
        name='privacy-policy'
    ),
]
