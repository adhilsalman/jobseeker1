from rest_framework import serializers
from app.models import User
class Login(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()
    