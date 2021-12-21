<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Meteor.html')

=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Meteor.html')

>>>>>>> 00a058feb37054fd60e37b3569dfe0169549379a
app.run(port = 3000)