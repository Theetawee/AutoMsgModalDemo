from django.contrib import admin
from .models import Schedule, Recipient

# Register your models here.


admin.site.register(Recipient)

from django import forms
from base.widgets import CheckboxSelectMultipleWidget


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"
        widgets = {
            "recipients": CheckboxSelectMultipleWidget,
            }


class ScheduleAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Schedule, ScheduleAdmin)
