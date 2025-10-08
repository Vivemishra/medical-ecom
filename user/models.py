from django.db import models

# Create your models here.
class tbl_orderlist(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=100,null=True)
    Mobile=models.IntegerField(max_length=10,null=True)
    City=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=200,null=True)
    NL=models.CharField(max_length=150,null=True)
    OS=models.CharField(max_length=150,null=True)