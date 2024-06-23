                                                          # Flask_Project




# What is the main purpose of `pip install flask`?
The main purpose of running the command pip install flask is to `install the Flask` web framework and its dependencies into your Python environment. Flask is a lightweight WSGI web application framework that allows you to build web applications and APIs quickly and easily. 

# 1. Set Up  Environment
`Install Python`: Ensure Python is installed on your system.
`Install pip`: Ensure pip, the Python package manager, is installed. It often comes with Python installations.
                         CMD : `python -m venv venv`
`Create a Virtual Environment`: It is good practice to create a virtual environment for your project to manage dependencies.
`Activate the Virtual Environment`:  To write this command `venv\Scripts\activate`

# 2. Install Flask
With  virtual environment activated, install Flask: Using this command `pip install Flask`
`Install Flask`: The command installs the Flask package, which provides the core functionality for creating web applications, such as routing, request handling, and response generation.

# Step 3: Install MySQL and set up a local database
Create a database named users ->  `create database users ;` 
Use the users Database ->    `use users;`
Create a table users Structure  ->     create table users (
                                ->            id INT AUTO_INCREMENT PRIMARY KEY,`
                                ->            name VARCHAR(80) NOT NULL,
                                ->            email VARCHAR(120) NOT NULL,
                                ->           role VARCHAR(80) NOT NULL
                                ->       );

users table with columns: id, name, email, and role
`Primary key` : A primary key is a field  in a database table that uniquely identifies each record in that table 
               -> Every value of the primary key must be unique.
               -> A primary key cannot contain NULL values
               -> Once a record is created, its primary key should not change     
`auto-increment`: meaning it will automatically increment for each new record.     

Insert the  data ->  `insert into users (name, email, role) VALUES`
                   ->  `('John Doe', 'john@example.com', 'Admin');`
Retrieve all users -> `SELECT * FROM users;`
Retrieve a specific user by ID -> `SELECT * FROM users WHERE id = 1`

# Step 4: connections with pip,python and mysql
Command: `pip install Flask mysql-connector-python`
 This is a MySQL driver for Python. It allows Python programs to connect to and interact with MySQL databases. By including `mysql-connector-python` in the install command, you're instructing `pip` to download and install the MySQL connector package and its dependencies.

# step 5: Create the app.py file:

  # a. Importing Necessary Modules 
 `from flask import Flask, render_template, request, redirect, url_for`
  `import mysql.connector`
  `from mysql.connector import Error`
  
  This imports the necessary modules. 
  `Flask` is the core module for creating a Flask application. 
  `render_template ` is used for rendering HTML templates,
  ` request` is for handling incoming request data, redirect is for redirecting users to a different endpoint, and `url_for` is for building a URL to a specific function.
  ` mysql.connector` and `Error` are used to connect to and handle errors from the MySQL database.


  # b. Initializing the Flask Application
 `app = Flask(__name__)`
  This creates an instance of the Flask class. This instance will be the WSGI (Web Server Gateway Interface) application and will handle incoming web requests.

  # c. Defining the Database Connection Function
   def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='users',
        user='root',
        password='Siva@2001'
    )
 
   This function,`get_db_connection` , is defined to establish a connection to the MySQL database.
  `mysql.connector.connect()` is used to connect to the database with the following parameters:
   `host`: The hostname of the database server, which is localhost in this case.
   `database`: The name of the database to connect to, which is users.
   `user`: The username to authenticate with, which is root.
   `password`: The password to authenticate with, which is Siva@2001.
   This function returns a connection object that can be used to interact with the MySQL database.

  # d. Defining the /hello Route  
   @app.route('/hello')
   def hello():
     return "Hello, World!"

    A simple route that returns "Hello, World!" when accessed.

  # e. Defining the /users Route   
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

    -> A route to display all users from the users table in the database.
    -> Connects to the database, fetches all user records, closes the connection, and renders the users.html template with the fetched user data.
    -> If there is an error, it returns the error message.   

   # f. Defining the /new_user Route  
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


    -> A route for adding a new user to the database.
    -> If the request method is POST, it retrieves form data, inserts it into the users table, commits the transaction, and redirects to the /users route.
    -> If there is an error, it returns the error message.
    -> For GET requests, it renders the new_user.html template.  

  # g. Defining the /users/<int:id> Route    
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

    -> A route to display details of a specific user by their ID.
    -> Connects to the database, fetches the user record with the specified ID, closes the connection, and renders the user_detail.html template with the fetched user data.
    -> If the user is not found, it returns a 404 error with the message "User not found".
    -> If there is an error, it returns the error message.

  # h. Custom Error Handler for 404
  @app.errorhandler(404)
  def page_not_found(error):
      return 'Page not found', 404

      -> Runs the Flask application in debug mode, which provides detailed error messages and automatically reloads the server on code changes.

 # This application provides routes for greeting, displaying all users, adding new users, viewing details of a specific user, and handling 404 errors.

 # 6.  HTML Template (templates/users.html):
   -> Create a directory named templates inside flask_app.
   -> Create a file named users.html and add the following HTML code:

   # Testing Routes: Access the routes in your browser:

       /hello     -> Its shows "Hello world!"
       /users     -> Its shows "All the Users List"
       /new_user  -> Its shows " You Create new user list"
       /users/1   -> Its shows "Retrieve a specific user by ID"

`GitHub`
 1. Create  Git repository for a Flask_project aafter choose or tick the add a `README file`
 `README file`: This file use the can write a long description for your project
 `main`: main branch is a secure branch don't allow the commits that causes the create a new branch is called a development branch,new branch name is `steptech_assignment`.
 after the branch and copy the link
 -> In desktop open the Command prompt: `git clone paste the link`
   `git clone`: create the  Flask_project in desktop  
 -> Command prompt: `code .`open the vs code
 -> In terminal to  check the  `git status`: its shows the red colour your files this is called no file add the github after the that 
 -> to `git add .` after adding to check the git status its show  green colour after that 
 -> `git commit -m " implement the Flask API and database functionality " `  to commit the main branch after that push the `main ` branch
 -> to check the origin use `git remote -v` after that `git push origin` 
 its over 



 # Its successfully completed this project , I am enjoying this working the project









  

   

 


   


                 
