from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route('/apples')
def apples():
  return 'apples'

app.run(host='0.0.0.0', port=8080)