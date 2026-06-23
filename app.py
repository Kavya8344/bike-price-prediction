from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()