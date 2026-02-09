from flask import (
    Flask, request, render_template, redirect, url_for, session, abort
)
from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime, ForeignKey,
    UniqueConstraint, and_
)
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'

# Database setup
engine = create_engine('sqlite:///todo.db', echo=True)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)
db_session = Session()

# User model (separate from blog app but same structure)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

# Todo models


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=True)

    user = relationship('User', backref='todos')
    tag = relationship('Tag', backref='todos')


class TodoLink(Base):
    __tablename__ = 'todolink'
    id = Column(Integer, primary_key=True)
    from_todo_id = Column(Integer, ForeignKey('todo.id'), nullable=False)
    to_todo_id = Column(Integer, ForeignKey('todo.id'), nullable=False)
    __table_args__ = (UniqueConstraint(
        'from_todo_id', 'to_todo_id', name='unique_todo_link'),)

# Authentication helpers


def get_current_user():
    if 'user_id' in session:
        return db_session.query(User).filter(
            User.id == session['user_id']).first()
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
    tag_id = request.args.get('tag_id', type=int)
    current_user = get_current_user()

    todos_query = db_session.query(Todo).filter(
        Todo.user_id == current_user.id)
    if tag_id:
        todos_query = todos_query.filter(Todo.tag_id == tag_id)

    todos = todos_query.order_by(Todo.created_at.desc()).all()
    tags = db_session.query(Tag).all()

    return render_template('index.html', todos=todos, tags=tags,
                           selected_tag_id=tag_id, current_user=current_user)


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
                return render_template(
                    'auth.html', error='Username already taken')

        elif action == 'login':
            user = db_session.query(User).filter(
                and_(User.username == username,
                     User.password == password)).first()
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


@app.route('/todo/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def todo_detail(todo_id):
    todo = db_session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        abort(404)

    all_tags = db_session.query(Tag).all()
    current_user = get_current_user()
    all_todos = db_session.query(Todo).filter(
        Todo.user_id == current_user.id).all()

    # Get linked todos
    linked_todo_ids = db_session.query(TodoLink.to_todo_id).filter(
        TodoLink.from_todo_id == todo_id).all()
    linked_todo_ids = [link[0]
                       for link in linked_todo_ids]  # Extract IDs from tuples
    linked_todos = db_session.query(Todo).filter(
        Todo.id.in_(linked_todo_ids)).all()

    if request.method == 'POST':
        # Handle adding tag
        if 'tag_id' in request.form:
            tag_id = request.form.get('tag_id', type=int)
            todo.tag_id = tag_id if tag_id else None
            db_session.commit()
            return redirect(url_for('todo_detail', todo_id=todo.id))

        # Handle linking to another todo
        elif 'link_todo_id' in request.form:
            link_todo_id = request.form.get('link_todo_id', type=int)
            if link_todo_id != todo.id:  # Prevent self-linking
                link = TodoLink(from_todo_id=todo.id, to_todo_id=link_todo_id)
                try:
                    db_session.add(link)
                    db_session.commit()
                except:
                    # Handle duplicate constraint
                    db_session.rollback()
                    pass
            return redirect(url_for('todo_detail', todo_id=todo.id))

    return render_template('todo_detail.html', todo=todo, all_tags=all_tags,
                           all_todos=all_todos, linked_todos=linked_todos,
                           current_user=current_user)


@app.route('/todo/new', methods=['POST'])
@login_required
def new_todo():
    title = request.form['title']
    current_user = get_current_user()
    if not title:
        return redirect(url_for('auth'))
    todo = Todo(title=title, user_id=current_user.id)
    db_session.add(todo)
    db_session.commit()
    return redirect(url_for('index'))


@app.route('/tags')
def tags():
    tags = db_session.query(Tag).all()
    current_user = get_current_user()
    return render_template('tags.html', tags=tags, current_user=current_user)


@app.route('/tag/new', methods=['POST'])
@login_required
def new_tag():
    name = request.form['name']
    tag = Tag(name=name)
    try:
        db_session.add(tag)
        db_session.commit()
    except:
        # Handle duplicate constraint
        db_session.rollback()
        pass
    return redirect(url_for('tags'))


@app.route('/tag/<int:tag_id>')
def tag_todos(tag_id):
    tag = db_session.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        abort(404)
    todos = db_session.query(Todo).filter(
        Todo.tag_id == tag_id).order_by(Todo.created_at.desc()).all()
    current_user = get_current_user()
    all_tags = db_session.query(Tag).all()
    return render_template('index.html', todos=todos, tags=all_tags,
                           selected_tag_id=tag_id, current_user=current_user)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5002)
