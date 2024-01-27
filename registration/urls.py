# urls.py in your app
from django.urls import path
from .views import submit_form, success_page

urlpatterns = [
    path('register/', submit_form, name='register_form'),
    path('success/', success_page, name='success_page'),
]
