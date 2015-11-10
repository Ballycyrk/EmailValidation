from flask import Flask, flash, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
import re
from time import gmtime, strftime
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key="emailtime"
mysql = MySQLConnector('emaildb')
emails = mysql.fetch('SELECT * FROM emails')
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/validate', methods=['POST'])
def validate():
  if not EMAIL_REGEX.match(request.form['email']):
    flash('Please Enter a valid email address.')
    return redirect('/')
  else:
    insert = "INSERT INTO emails (email, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(request.form['email'])
    mysql.run_mysql_query(insert)
    return render_template('success.html', emails = emails)
app.run(debug=True)

