from flask import Flask, request, render_template, redirect, url_for, session, abort
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'

# Database setup
engine = create_engine('sqlite:///blog.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()

# Models
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', backref='posts')
    # comments and likes will be accessed via queries

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    user = relationship('User', backref='comments')

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'post_id', name='unique_user_post_like'),)

    user = relationship('User', backref='likes')

# Authentication helpers
def get_current_user():
    if 'user_id' in session:
        return db_session.query(User).filter(User.id == session['user_id']).first()
    return None

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Routes
@app.route('/')
def index():
    posts = db_session.query(Post).join(User).order_by(Post.created_at.desc()).all()
    current_user = get_current_user()
    return render_template('index.html', posts=posts, current_user=current_user)

@app.route('/user/<int:user_id>')
def user_posts(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        abort(404)
    posts = db_session.query(Post).filter(Post.user_id == user_id).order_by(Post.created_at.desc()).all()
    current_user = get_current_user()
    return render_template('user_posts.html', posts=posts, user=user, current_user=current_user)

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action']  # 'login' or 'register'

        if action == 'register':
            # Simple registration without password hashing
            user = User(username=username, password=password)
            try:
                db_session.add(user)
                db_session.commit()
                session['user_id'] = user.id
                session.permanent = True
                return redirect(url_for('index'))
            except:
                db_session.rollback()
                return render_template('auth.html', error='Username already taken')

        elif action == 'login':
            user = db_session.query(User).filter(and_(User.username == username, User.password == password)).first()
            if user:
                session['user_id'] = user.id
                session.permanent = True
                return redirect(url_for('index'))
            else:
                return render_template('auth.html', error='Invalid credentials')

    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        current_user = get_current_user()
        post = Post(title=title, content=content, user_id=current_user.id)
        db_session.add(post)
        db_session.commit()
        return redirect(url_for('index'))

    return render_template('new_post.html')

@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = db_session.query(Post).filter(Post.id == post_id).first()
    if not post:
        abort(404)
    content = request.form['content']

    current_user = get_current_user()
    comment = Comment(content=content, user_id=current_user.id, post_id=post_id)
    db_session.add(comment)
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/post/<int:post_id>/like', methods=['POST'])
@login_required
def add_like(post_id):
    post = db_session.query(Post).filter(Post.id == post_id).first()
    if not post:
        abort(404)

    current_user = get_current_user()
    # Check if user already liked this post
    existing_like = db_session.query(Like).filter(and_(Like.user_id == current_user.id, Like.post_id == post_id)).first()
    if not existing_like:
        like = Like(user_id=current_user.id, post_id=post_id)
        db_session.add(like)
        db_session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5001)