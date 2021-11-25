from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/me')
def me():
    return render_template('users/mine.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/craftswithlucy')
def crafts():
    return render_template('users/crafts.html')

@app.route('/catsdaily')
def cats():
    return render_template('users/cats.html')

@app.route('/walkingonsunshine')
def nature():
    return render_template('users/nature.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
