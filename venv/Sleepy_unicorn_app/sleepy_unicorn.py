from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from blog_posts import blog_posts

app = Flask(__name__)

# Flask-Mail Configuration
#app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # Example: 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587  # Change to 465 for SSL
#app.config['MAIL_USE_TLS'] = True  # Use True for TLS, False for SSL
#app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Your email
#app.config['MAIL_PASSWORD'] = 'your-email-password'  # Your email password
#app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'

#mail = Mail(app)

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

"""
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(f"New Contact Form Submission from {name}",
                      sender=email,
                      recipients=['your-email@example.com'])  # Change to your recipient email
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
    
    """

   
if __name__ == '__main__':
    app.run(debug=True)
    