from flask import Flask, render_template, request
from stories import story
app = Flask(__name__)

@app.route('/')
def story_form_generator():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def story_generator():
    text = story.generate(request.args)
    return render_template('story.html', text=text)

