from flask import Flask, request, render_template, flash, redirect, session
from surveys import Survey, satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = "ooOOooOOooOoo-secret!"





@app.route("/")
def home():
    return render_template("home.html")

@app.route("/handleSession")
def handleSession():
    session['responses'] = []
    return redirect('/question/0')



@app.route("/question/<int:num>")
def question_display(num):
    responses = session['responses']
    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect("/complete")
    elif(len(responses) != num):
        flash(f"Invalid Question id {id}")
        return redirect(f"/question/{len(responses)}")
    else:
        question = satisfaction_survey.questions[int(num)].question
        num = int(num) + 1
        return render_template("question.html", question = question, num = num)

@app.route("/answer", methods={"POST"})
def handle_answer():
    answer = request.form['choice']
    #Handles session data
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    return redirect(f"question/{len(responses)}")


@app.route("/complete")
def completed():
    #restart responses list
    responses = []
    return "THANK YOU for completing the server!"
