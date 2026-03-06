from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

questions = [
    "요즘 가장 배우고 싶은 것은?",
    "오늘 가장 기분 좋았던 일은?",
    "어릴 때의 나에게 한마디 한다면?",
    "내가 가장 좋아하는 시간은 언제일까?",
    "지금의 나를 한 단어로 표현하면?"
]

users = []   # 회원 정보 저장
answers = [] # 답변 저장

@app.route("/")
def home():
    if "current_question" not in session:
        session["current_question"] = random.choice(questions)

    question = session["current_question"]
    username = session.get("username")

    return render_template("index.html", question=question, answers=answers, username=username)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users.append({
            "username": username,
            "password": password
        })

        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                return redirect("/")

        return "로그인 실패"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")


@app.route("/answer", methods=["POST"])
def answer():
    if "username" not in session:
        return redirect("/login")

    user_answer = request.form["answer"]

    answers.append({
        "username": session["username"],
        "content": user_answer,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/delete/<int:index>")
def delete(index):

    if "username" not in session:
        return redirect("/login")

    if answers[index]["username"] == session["username"]:
        answers.pop(index)

    return redirect("/")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if "username" not in session:
        return redirect("/login")

    if answers[index]["username"] != session["username"]:
        return "수정 권한이 없습니다."

    if request.method == "POST":
        new_answer = request.form["answer"]
        answers[index]["content"] = new_answer
        return redirect("/")

    return render_template("edit.html", answer=answers[index])

@app.route("/new-question")
def new_question():
    session["current_question"] = random.choice(questions)
    return redirect("/")