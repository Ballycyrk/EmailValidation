from flask import Flask, flash, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key="emailtime"
mysql = MySQLConnector('emaildb')
@app.route('/')
def index():
  emails = mysql.fetch('SELECT * FROM emails')
  print emails
  render_template('index.html')
