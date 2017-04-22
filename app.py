import logging

from random import randint

from flask import Flask, render_template, request, redirect

from flask_ask import Ask, statement, question, session



app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def start():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("YesIntent")

def next_round():
    round_msg = render_template('round')
    session.attributes['answers'] = 1
    return question(round_msg)

@ask.intent("MoveIntent")

def initRound():
    next_msg = render_template('Guess1')
    session.attributes['answers'] = int(session.attributes['answers']) + 1
    return question(next_msg)

@ask.intent("AnswerIntent", convert={'first': int})

def answer(first):
    if int(session.attributes['answers']) < 2:
        return statement("Invalid instruction")
    elif int(session.attributes['answers']) == 2:
        input = int(first)
        if input == 1:
            render question(render_template('compostResponse'))
        elif input == 2:
            render_question(render_template('recyclingResponse'))
        elif input == 3:
            render_question(render_template('recyclingResponse'))
        elif input == 4:

        elif input == 5:

    msg = render_template('win')
    return question(msg)

@ask.intent("CompostIntent")


if __name__ == '__main__':

    app.run(debug=True)
