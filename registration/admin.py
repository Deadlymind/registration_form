# admin.py
from django.contrib import admin
from .models import FormSubmission

class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'comments')
    search_fields = ('full_name', 'email', 'phone_number', 'comments')
    list_filter = ('full_name', 'email')
    ordering = ('-id',)  # Change to the field you want to use for sorting

# Register your models here.
admin.site.register(FormSubmission, FormSubmissionAdmin)
