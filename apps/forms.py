from django import forms


class SalesUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.PasswordField(label='Password', max_length=100)
    sales_id = forms.IntegerField(label='Sales', max_length=100)
