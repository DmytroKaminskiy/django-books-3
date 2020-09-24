
from django import forms
from user.models import User
from user.tasks import send_email_async


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

class ContactUsForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField()

    def save(self):
        subject = self.cleaned_data['subject']
        text = self.cleaned_data['text']
        send_email_async.delay(subject, text)

