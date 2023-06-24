from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
class MyCreationForm(UserChangeForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user