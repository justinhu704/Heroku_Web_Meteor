from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Meteor.html')
if_name_=="_main_":
    app.run

