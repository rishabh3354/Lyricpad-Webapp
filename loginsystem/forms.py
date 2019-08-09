from django import forms
from django.contrib.auth.forms import UserCreationForm
from loginsystem.models import Contact



class LoginForm(forms.Form):

    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Email or Mobile no.'}))
    password = forms.CharField(widget=forms.PasswordInput)

class UserCreateForm(UserCreationForm):

    username = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': 'Enter Email Address'}))

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ContactForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))

    class Meta:

        model = Contact
        fields = '__all__'

        # fields = ('clg_name', 'clg_email')
