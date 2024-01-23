"""
John Leckie, SDEV 300, 22 Sep '23

Astronomy Web App

This is a Flask web application for a simple astronomy website. It includes routes to
different pages and displays the current date and time on the homepage.

"""

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
