"""
John Leckie, SDEV 300, 22 Sep '23

Astronomy Web App

This is a Flask web application for a simple astronomy website. It includes routes to
different pages and displays the current date and time on the homepage.

"""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib  # Required for password hashing

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the provided password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the username and hashed password match any records in the file
        with open(user_data_file, 'r') as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(':')
                if username == stored_username and hashed_password == stored_hashed_password:
                    flash('Login successful', 'success')
                    return redirect(url_for('home'))

        flash('Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/')
def home():
    """
    Render the home page of the astronomy website.

    Returns:
        rendered template with current time
    """
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


@app.route('/telescope_time')
def telescope_time():
    """
    Render the telescope time sign-up page.

    Returns:
        rendered template for telescope time page
    """
    return render_template('telescope_time.html')


@app.route('/supercomputer_time')
def supercomputer_time():
    """
    Render the supercomputer time request page.

    Returns:
        rendered template for supercomputer time page
    """
    return render_template('supercomputer_time.html')


@app.route('/planetarium')
def planetarium():
    """
    Render the planetarium volunteer page.

    Returns:
        rendered template for planetarium volunteer page
    """
    return render_template('planetarium.html')


app.secret_key = 'your_secret_key'

# Store user data in a file
user_data_file = 'user_data.txt'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate password complexity
        if not (len(password) >= 12 and any(c.isupper() for c in password)
                and any(c.islower() for c in password) and any(c.isdigit() for c in password)
                and any(not c.isalnum() for c in password)):
            flash('Password does not meet complexity requirements', 'error')
        else:
            # Hash the password before storing it (for security)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Write user data to the file (append mode)
            with open(user_data_file, 'a') as file:
                file.write(f'{username}:{hashed_password}\n')

            flash('Registration successful', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run()
