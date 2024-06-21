from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='users',
        user='root',
        password='Siva@2001'
    )

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/users')
def users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('users.html', users=users)
    except Error as e:
        return str(e)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('users'))
        except Error as e:
            return str(e)
    return render_template('new_user.html')

@app.route('/users/<int:id>')
def user_detail(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            return render_template('user_detail.html', user=user)
        else:
            return "User not found", 404
    except Error as e:
        return str(e)
@app.errorhandler(404)
def page_not_found(error):
    return 'Page not found', 404        

if __name__ == '__main__':
    app.run(debug=True)
