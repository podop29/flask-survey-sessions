from flask import Flask, request, render_template, flash, redirect
from surveys import Survey, satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = "ooOOooOOooOoo-secret!"

#stores survey responses
responses = []


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/question/<int:num>")
def question_display(num):
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
    responses.append(answer)
    return redirect(f"question/{len(responses)}")


@app.route("/complete")
def completed():
    #restart responses list
    responses = []
    return "THANK YOU for completing the server!"
