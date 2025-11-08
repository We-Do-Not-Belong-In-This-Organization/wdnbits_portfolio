from flask import Flask, render_template, request 


app = Flask(__name__)


# HOME
@app.route('/')
def home():
    return render_template('index.html', header_title="Home Page")


if __name__ == '__main__':
    app.run(debug=True)
