# app/server.py
from flask import Flask, render_template
from create_app import create_app

app = create_app()

@app.route('/')
def home():
    return 'hello world'

@app.route('/about')
def about():
    return 'About'

@app.route('/blog')
def blog():
    posts = [
        {'title': "new world shows", 'author': "charlei"},
        {'title': "old show world", 'author': "maxwell"}
    ]
    return render_template('blog.html', author="Bob", sunny=True, posts=posts)

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return f'this is blog Post Number {blog_id}'

if __name__ == '__main__':
    app.run(debug=True)
