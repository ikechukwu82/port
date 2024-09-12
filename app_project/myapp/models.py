from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True) # Make message optional by adding blank=True
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Contact form {self.name}'

#Adding employee database
class Employee(models.Model):
    empno = models.CharField(max_length=20)
    empname = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    salary = models.IntegerField()
    joined_date = models.DateField(null=True)
    class Meta: 
        db_table = "employee"
    
    def _str_(self):
        return "Name: {}, Contact: {}".format(self.empname, self.contact)