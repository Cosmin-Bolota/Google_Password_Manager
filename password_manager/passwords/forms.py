from django.forms import ModelForm
from .models import UserPW


class PasswordForm(ModelForm):
    class Meta:
        model = UserPW
        fields = ['domain', 'pwd']

        labels = {
            'pwd': 'Password'
        }
