from django import forms


class BlogForm(forms.Form):
    date = forms.DateField(label='Date')
    autor = forms.CharField(max_length=50, min_length=5, label='Autor')
    title = forms.CharField(max_length=50, min_length=10, label='Title')
    subtitle = forms.CharField(max_length=50, min_length=5, label='Subtitle')
    body = forms.CharField(max_length=500, label='Body')