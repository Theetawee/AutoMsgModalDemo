from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import Account
# Create your models here.


class Recipient(models.Model):
    phone = PhoneNumberField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.phone}'


class Schedule(models.Model):
    REPEAT_OPTIONS=(
        ('D','Daily'),
        ('W','Weekly')
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    recipients = models.ManyToManyField(Recipient,blank=True)
    sender=models.ForeignKey(Account,on_delete=models.CASCADE)
    repeat=models.CharField(choices=REPEAT_OPTIONS,max_length=1,default='W')
    send_at = models.TimeField(verbose_name='Message send at')

    def __str__(self):
        return self.message[:20]
