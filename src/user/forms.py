
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

    def save(self, commit=True):
        # forms.ModelForm.save(self, commit)
        print('User Form Before Save')
        user = super().save(commit=False)
        user.email = user.email.lower()
        user.first_name = user.first_name.title()
        user.last_name = user.last_name.title()
        user.save()
        print('User Form After Save')
        return user

