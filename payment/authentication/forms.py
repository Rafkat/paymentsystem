from django import forms


class NewUser(forms.Form):
    user_name = forms.CharField(max_length=100, label='Name:')
    password = forms.SlugField(max_length=50, label='Password:')

