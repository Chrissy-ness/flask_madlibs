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
    
    return render_template("home.html", words=list_of_words)

@app.route('/story')
def my_story():
    """Show the story on another route"""
    text = story.generate(request.args)
    return render_template("story.html", story=text)
