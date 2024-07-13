from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('users-cart/', views.UsersCartView.as_view(), name='users-cart'),
]
