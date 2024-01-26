from rest_framework.serializers import ModelSerializer
from .models import Account



class AccountSerializer(ModelSerializer):
    class Meta:
        model=Account
        fields=['username','name','email','location','api_key','api_token','platform','payment_plan']


