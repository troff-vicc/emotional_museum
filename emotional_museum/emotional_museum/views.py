from django.shortcuts import render
from .forms import NameForm

def index(request):
    return render(request, 'home.html')
def login(request):
    def checkString(x):
        s = 'abcdefghijklmnopqrstuvwxyz_1234567890'
        x = x.lower()
        t = True
        for i in x:
            if not(i in s):
                t = False
        return t
    def checkName(cur):
        cur.execute(f'''SELECT name from login WHERE name = "{name}" ''')
        if cur.fetchall() == []:
            if checkString(name):
                return [True, '']
            else:
                return [False, 'Логин может состоять из латиницы, чисел или нижнего подчёркивания ']
        else:
            return [False, 'Логин уже занят']
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
                email = email.replace('@', '|')
                clas = form.cleaned_data['clas']
                con = sqlite3.connect('emotional_museum/emotional_museum/emotional_museum.db')
                cur = con.cursor()
                checkName = checkName(cur)
                if checkName[0]:
                    cur.execute(f'''SELECT name from login;''')
                    cur.execute(f"""INSERT INTO login VALUES(?, ?, ?, ?, ?);""", (len(cur.fetchall()), name, password, email, clas))
                    con.commit()
                else:
                    out = checkName[1]
            else:
                if password1 != password:
                    out = 'Пароли не совпадают'
                else:
                    out = 'Пароль должен быть длинее 8 символов'
    else:
        form = NameForm()
    return render(request, 'login.html', {'form': form, 'out': out})