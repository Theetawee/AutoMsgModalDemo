from rest_framework.serializers import ModelSerializer
from .models import Schedule,Recipient
from accounts.serializers import AccountSerializer




class RecipientSerializer(ModelSerializer):
    class Meta:
        model=Recipient
        fields="__all__"


class ScheduleSerializer(ModelSerializer):
    sender=AccountSerializer()
    recipients=RecipientSerializer(many=True)
    class Meta:
        model=Schedule
        fields=['recipients','sender','message','created_at','repeat','send_at','id']

