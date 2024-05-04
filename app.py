from flask import Flask,  request, redirect, url_for, render_template
import random

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == '123':
            return redirect(url_for('protected'))
        else:
            return 'Wrong password. Please try again.'
    return render_template('login.html')

@app.route('/protected')
def protected():
    return 'Access granted!'



@app.route("/")
def main():
    return render_template('main.html')


@app.route('/blog')
def blog():
    fw = open('news.txt', 'r')
    news = fw.read().split('\n')
    fw.close()
    random.shuffle(news)
    return render_template('blog.html', news=news)


@app.route('/contacts')
def contact():
    return render_template('contacts.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
