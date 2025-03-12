from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from blog_posts import blog_posts

app = Flask(__name__)

# page adresses
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/start-here')
def start_here():
    return render_template('start_here.html', title="Start Here")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=blog_posts)

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("blog_post.html", post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



   
if __name__ == '__main__':
    app.run(debug=True)
    