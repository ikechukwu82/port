from django.contrib import admin
from .models import Contact
from .models import Employee

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')
    search_fields = ('name', 'email')
    
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("empname", "contact", "joined_date")
    search_fields = ("empname__startswith", )
# Register your models here.
