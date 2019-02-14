from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage_input_form():
    prompts = []
    stories = ["", "", ""]

    newStory = Story(prompt, story)
    return render_template('form.html', list_of_prompts=story.prompts)

@app.route('/story')
def create_story():
    html = story.generate(request.args)

    return render_template('story.html', generate_story=html)