from djongo import models

# Create your models here.
class Documents(models.Model):
    name=models.CharField(max_length=50)
    extenesion=models.CharField(max_length=4)
    create_date=models.DateTimeField(auto_now=True)
