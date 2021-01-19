from django import forms

from .models import *


# Форма отправки сообщения через почту
class SendMailToConsoleForm(forms.Form):
    email = forms.EmailField(max_length=150, min_length=4,
                             help_text='Введите ваш email')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=False)

    email.widget.attrs.update({'class': 'form-control', 'required': 'required'})
    message.widget.attrs.update({'class': 'form-control', 'rows': '3',
                                'required': 'required'})
