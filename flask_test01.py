from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the homepage.  Flask tutorial 1."

@app.route('/about')
def about():
    return '<h2>This would be an example of the about page.</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post ID is %s" % post_id


if __name__ == '__main__':
    app.run(port=9000, debug=True)