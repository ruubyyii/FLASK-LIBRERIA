from flask import Flask, render_template, url_for, redirect, flash, request
from flask_myseqldb import MySQL
from werkzeug.segurity import generate_password_hash, check_password_hash
from config import config

app = Flask(__name__)

mysql = MySQL(app)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()