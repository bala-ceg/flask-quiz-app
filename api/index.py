from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame({
    'Question': [
        "What is the capital of France?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the chemical symbol for water?"
    ],
    'Answer': [
        "Paris",
        "Shakespeare",
        "H2O"
    ]
})

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=df.to_dict(orient='records'))


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
