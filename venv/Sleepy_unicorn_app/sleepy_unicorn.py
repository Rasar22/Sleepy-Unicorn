from flask import Flask, render_template

app = Flask(__name__)

# page adresses
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/start-here')
def start_here():
    return render_template('start_here.html', title="Start Here")

@app.route('/blog')
def about():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



   
if __name__ == '__main__':
    app.run(debug=True)
    