from django.urls import path

from .views import registeration, custom_login, custom_logout

urlpatterns = [
    path('registration/', registeration, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]