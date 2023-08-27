# © ZiB BoTs 
# a file for web deploys

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ZiB_BoTs'


if __name__ == "__main__":
    app.run()
