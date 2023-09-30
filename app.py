"""
John Leckie, SDEV 300, 22 Sep '23

Astronomy Web App

This is a Flask web application for a simple astronomy website. It includes routes to
different pages and displays the current date and time on the homepage.
"""

import hashlib  # Required for password hashing
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = '123456789'

# Store user data in a file
USER_DATA_FILE = 'user_data.txt'


def register():
    """
    Register users and store their information in a text file after validation.

    Returns:
        rendered template for registration page with flash messages
    """
    flash('', 'error')  # Clears existing flash messages for the session, if any
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists in the file
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                stored_username, _ = line.strip().split(':')
                if username == stored_username:
                    flash('Username already exists. Please choose another username or return '
                          'to Login via below link.', 'error')
                    return render_template('register.html')

        # Validate password complexity
        if not (len(password) >= 12 and any(c.isupper() for c in password)
                and any(c.islower() for c in password) and any(c.isdigit() for c in password)
                and any(not c.isalnum() for c in password)):
            flash('Password does not meet complexity requirements', 'error')
        else:
            # Hash the password before storing it (for security)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Write user data to the file (append mode)
            with open(USER_DATA_FILE, 'a', encoding='utf-8') as file:
                file.write(f'{username}:{hashed_password}\n')
                flash('Registered! Return to Login below.', 'success')

    return render_template('register.html')


def login():
    """
    Authenticate users and log them in if valid credentials are provided.

    Returns:
        rendered template for login page with flash messages
    """
    flash('', 'error')  # Clears existing flash messages for the session, if any
    reg_message = session.pop('reg_message', None)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the provided password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the username and hashed password match any records in the file
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:  # Opens file in read mode
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(':')
                if username == stored_username and hashed_password == stored_hashed_password:
                    flash('Login successful', 'success')
                    session['logged_in'] = True  # Sets session as logged in. Important.
                    return redirect(url_for('home'))

        flash('Invalid username or password', 'error')

    return render_template('login.html', reg_message=reg_message)


def home():
    """
    Render the home page of the astronomy website.
    Redirects the user to the login page if they are not logged in.

    Returns:
        rendered template with current time
    """
    # Check if the user is logged in, if not, redirect to the login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


def telescope_time():
    """
    Render the telescope time sign-up page.

    Returns:
        rendered template for telescope time page
    """
    # Check if the user is logged in, if not, redirect to the login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('telescope_time.html')


def supercomputer_time():
    """
    Render the supercomputer time request page.

    Returns:
        rendered template for supercomputer time page
    """
    # Check if the user is logged in, if not, redirect to the login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('supercomputer_time.html')


def planetarium():
    """
    Render the planetarium volunteer page.

    Returns:
        rendered template for planetarium volunteer page
    """
    # Check if the user is logged in, if not, redirect to the login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('planetarium.html')


def logout():
    """
    Log users out by clearing their session data.

    Returns:
        Redirects to the login page with a logout flash message
    """
    # Clear the user's session data to log them out
    session.clear()
    flash('Logout Successful!', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
