from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post



posts =[

    {
        'author': 'nananatiar',
        'title': 'Cara MUDAH Menjadi Kaya, Nomer 5 Sangat Mencengangkan!',
        'content': 'Lorem ipsum',
        'date_posted': 'February 30, 2020'
    },
    {
        'author': 'Jontel De La Conschantel',
        'title': 'Ternyata Kentang Banyak Manfaatnya, Manfaat Ke-5 Orang Jarang yang Tahu',
        'content': 'Second post content',
        'date_posted': 'October 23, 2020'
    }

]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() :
        flash(f'Akun berhasil dibuat untuk {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Anda Berhasil Masuk!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Gagal. Silahkan Periksa Kembali Username dan Password', 'danger')
    return render_template('login.html', title='Login', form=form)