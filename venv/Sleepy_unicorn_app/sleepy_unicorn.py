from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/start-here')
def start_here():
    return render_template('start_here.html', title="Start Here")

if __name__ == '__main__':
    app.run(debug=True)
    