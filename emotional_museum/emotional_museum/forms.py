from django import forms

class NameForm(forms.Form):
    GEEKS_CHOICES = (
        'Посититель',
        'Музей'
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