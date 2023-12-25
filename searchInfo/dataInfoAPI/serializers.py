from rest_framework import serializers
from dataInfo.models import User, Documents

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','email', 'password','first_name','last_name', 'is_staff')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documents
        fields=('id','name', 'extenesion','create_date','id_user', 'my_file', 'url')

class SheredFilesSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id_doc','name_doc', 'id_user_from', 'id_user_to')