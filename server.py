from flask import Flask, flash, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
import re
from time import gmtime, strftime
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key="emailtime"
mysql = MySQLConnector('emaildb')
@app.route('/')
def index():
  emails = mysql.fetch('SELECT * FROM emails')
  return render_template('index.html')
@app.route('/validate', methods=['POST'])
def validate():
  if not EMAIL_REGEX.match(request.form['email']):
    flash('Please Enter a valid email address.')
    return redirect('/')
  else:
    return render_template('success.html')
app.run(debug=True)

