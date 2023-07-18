from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "NFAQJQL"
debug = DebugToolbarExtension(app)

@app.route('/')
def ask_questions():
    """Show a form with iput requirements taken from the provided STORY INSTANCE"""
    list_of_words = story.prompts
    text = story.template

    return render_template("home.html", words=list_of_words, text=text)

@app.route('/story')
def my_story():
    """
    - This view function is responsible for generating an html template that shows the results of the input elements after the submit button is clicked. 
    - It will also check if the inputs sent by the user passes the requirements of having atleast '3 letters'.
    - If the user's input values does not pass, the user will remain/returned to the home route, and a message will be generated to alert the user of the problem.
    """
    key_vals = request.args
    validity = True

    text = story.generate(key_vals)
    for (key, val) in key_vals.items():
        if len(val) == 0 or len(val) < 3:
            validity = False

    print(f"This is the validity:{validity}...")
    if validity == False:
        return render_template("value_error.html", words=list_of_words)

    return render_template("story.html", story=text)
