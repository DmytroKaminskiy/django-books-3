
from django import forms
from user.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'age',
        )
