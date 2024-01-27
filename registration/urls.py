# urls.py in your app
from django.urls import path
from .views import submit_form, success_page

urlpatterns = [
    """
    URL pattern for submitting the registration form.

    Example:
    - http://yourdomain.com/register/
    """
    path('register/', submit_form, name='register_form'),

    """
    URL pattern for displaying the success page after form submission.

    Example:
    - http://yourdomain.com/success/
    
    Note: 'success_page' should match the name used in the redirect.
    """
    path('success/', success_page, name='success_page'),
]
