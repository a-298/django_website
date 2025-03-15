from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    birth_date = forms.DateField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class SignInForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
