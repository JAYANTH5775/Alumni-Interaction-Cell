from flask import Flask,render_template, request,redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234567890'
app.config['MYSQL_DB'] = 'alumni'
 
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html') 

@app.route('/signup', methods = ['POST', 'GET'])
def signup(): 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['Email_id']
        password = request.form['password']
        Repassword = request.form['Repassword']
        cursor = mysql.connection.cursor()
        # if password!=Repassword:
        #     return "<h1> passwords are not matching</h1>"
        cursor.execute("INSERT INTO student_registration (Sname,Email_id,Password) VALUES (%s, %s, %s)",(name,email,password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('Main'))
    return render_template('stureg.html')

@app.route('/main home')
def Main():
    return render_template("main.html")

@app.route("/signup as alumni", methods = ['POST', 'GET'])
def signupA(): 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['Email_id']
        password = request.form['password']
        Repassword = request.form['Repassword']
        cursor = mysql.connection.cursor()
        # if password!=Repassword:
        #     return "<h1> passwords are not matching</h1>"
        cursor.execute("INSERT INTO alumni (Sname,Email_id,Password) VALUES (%s, %s, %s)",(name,email,password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('Main'))
    return render_template('stureg.html')


 
app.run(host='localhost', port=5000,debug=True)