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

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
