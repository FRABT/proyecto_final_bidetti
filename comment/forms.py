from django import forms


class CommentForm(forms.Form):
    date = forms.DateField(label='Date')
    title = forms.CharField(max_length=50, min_length=10, label='Title')
    body = forms.CharField(max_length=500, label='Body')