from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_worlld():
    return 'Hello Docker-World!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')