from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    create_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'T_USER'
        ordering = ['create_date']
