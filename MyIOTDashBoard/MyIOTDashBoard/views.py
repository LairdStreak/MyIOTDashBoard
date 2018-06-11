"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MyIOTDashBoard import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route("/api/user/<int:user_id>", methods=["GET"])
def user_show(user_id):
    """
    This function shows a particular user.
    """
    #return a particular user
    print("Retrieve user #{}".format(user_id))
    result = user_get(user_id)
    return Response(json.dumps(result), mimetype="application/json")


def user_get(user_id):
    """
    This function retrieves a user's information.
    :param user_id: user ID
    :type user_id: int
    """
    #prepare result
    json = {}
    results = []
    temp = {}
    #get _all_ the information
    temp[row[0]] = {}
    temp[row[0]]["id"] = "1"
    temp[row[0]]["name"] = "test"
    temp[row[0]]["mail"] = "test2"
    results.append(temp[row[0]])
    json["results"] = results
    return json
