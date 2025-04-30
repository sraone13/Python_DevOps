from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
    return 'helloworld'

app.run("0.0.0.0")

