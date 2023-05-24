from flask import Flask

app = Flask("Testing")

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == "main":
    app.run(debug=True)