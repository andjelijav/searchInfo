from djongo import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class DocumentManager(models.Manager):
    def upload_document(self, name, extenesion,create_date, id_user_):
        #print(id_user)
        document=self.model(name=name,
        extenesion=extenesion,
        create_date=create_date,
        id_user=id_user_)
               
        return document
    
    

class Documents(models.Model):
    name=models.CharField(max_length=50)
    extenesion=models.CharField(max_length=4)
    create_date=models.DateTimeField(auto_now=True)
    id_user=models.CharField(max_length=30, default='guest', unique=False)
    my_file=models.FileField(upload_to='./dokumenti', default='.')
    url=models.CharField(max_length=100)

    

    objects = DocumentManager() 
    
    def __str__(self):
        return self.name
    
    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,first_name=None,last_name=None, **extra_fields):
        #if not email:
            #raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email, password, extra_fields)

    

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    is_active= models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects=UserManager()

    def __str__(self):
        return self.email


class ShereFilesManager(models.Manager):
    def shereDoc(self, id_doc, name_doc, id_user_from, id_user_to):
        file=self.model(id_doc=id_doc, name_doc=name_doc, id_user_from=id_user_from, id_user_to=id_user_to)
        return file


class SheredFiles(models.Model):
    id_doc=models.CharField(max_length=30)
    name_doc=models.CharField(max_length=30)
    id_user_from=models.CharField(max_length=30)
    id_user_to=models.CharField(max_length=30)

    objects=ShereFilesManager()

    def __str__(self):
        return self.name_doc
