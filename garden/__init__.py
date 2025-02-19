import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session

def create_app():

    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    app = Flask(__name__)
    # app.config['TESTING'] = True
    app.config['SECRET_KEY'] = os.environ.pop('SECRET_KEY')
    app.config['DATABASE'] = os.path.join(app.instance_path, 'user.sqlite')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        if not 'user_id' in session:
            return redirect(url_for('auth.login'))
        return render_template('index.html')

    return app

