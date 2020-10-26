from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '17122ffe8ca9b478c20a13bc651d3a4beb02d634257d013d7f37434ab2d3a5ec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model) :
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


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
if __name__ =='__main__' :
    app.run(debug=True)