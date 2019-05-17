from flask import Flask, render_template
from view.temperature import temperature

app = Flask(__name__)

app.register_blueprint(temperature, url_prefix='/temperature')

@app.route('/')
def helloworld():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
