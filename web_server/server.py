from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/<username>/<int:post_id>')
# def users_post(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)

@app.route('/works')
def works():
    return render_template('./works.html')

@app.route('/work')
def work():
    return render_template('./work.html')

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/contact')
def contact():
    return render_template('./contact.html')

@app.route('/components')
def components():
    return render_template('./components.html')

@app.route('/favicon.ico')
def icon():
    return 'This is the contact page'