from flask import Flask
import jinja2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
env = jinja2.Environment()
env.globals.update(zip=zip)


from routes import *
if __name__ == "__main__":
    app.run(debug=True)