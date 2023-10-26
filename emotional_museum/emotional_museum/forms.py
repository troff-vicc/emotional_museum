from django import forms

class logupForm(forms.Form):
    GEEKS_CHOICES = (
        ('0', 'Посититель'),
        ('1', 'Музей')
    )
    name = forms.CharField(label_suffix=False, label='', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.CharField(label_suffix=False, label='', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(label_suffix=False, label='', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))
    password1 = forms.CharField(label_suffix=False, label='', max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Повторите пароль'}))
    clas = forms.ChoiceField(choices=GEEKS_CHOICES)
class loginForm(forms.Form):
    name = forms.CharField(label_suffix=False, label='', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label_suffix=False, label='', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))