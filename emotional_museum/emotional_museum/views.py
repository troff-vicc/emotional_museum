from django.shortcuts import render
from .forms import NameForm

def index(request):
    return render(request, 'home.html')
def login(request):
    def check(name):
        cur.execute(f'''SELECT name from emotional_museum WHERE sportsman = "{name}" ''')
        if cur.fetchall() == []:
            return True
        else:
            return False
    out = ''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            if len(password) >= 8 and password1 == password:
                import sqlite3
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                clas = form.cleaned_data['clas']
                con = sqlite3.connect('emotional_museum.db')
                cur = con.cursor()
                if check(name):
                    cur.execute(f'''SELECT name from emotional_museum;''')
                    cur.execute(f"INSERT INTO emotional_museum VALUES({len(cur.fetchall())+1, name, password, email, clas});")
                    con.commit()
                else:
                    out = 'Логин уже занят'
            else:
                if password1 != password:
                    out = 'Пароли не совпадают'
                else:
                    out = 'Пароль должен быть длинее 8 символов'
    else:
        form = NameForm()
    return render(request, 'login.html', {'form': form, 'out': out})