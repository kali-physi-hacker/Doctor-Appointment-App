from django import forms
from django.contrib.auth import get_user_model

from appointment.models.doctor import Doctor


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=200)


class RegisterForm(forms.ModelForm):

    password = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "password2")

    def clean_password(self):
        """
        Return the password if both password and password is the same
        Raise validationError otherwise
        :return:
        """
        data = self.data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Password Mismatch")
        return data['password']

    def clean_email(self):
        return self.cleaned_data.get("email").lower()
