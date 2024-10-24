from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.get("/")
def index():
    context = {
        "question": "Яка мова програмування тобі найбільше подобається?",
        "answers": ["Python", "JS", "Java", "C++", "C#", "Basic"]
    }
    return render_template("index.html", **context)

@app.get("/add_vote/")
def add_vote():
    vote = request.args.get("answer")
    with open("data/answers.txt", "a", encoding="utf-8") as file:
        file.write(vote + "\n")

    return redirect(url_for("results"))


@app.get("/results/")
def results():
    with open("data/answers.txt", "r", encoding="utf-8") as file:
        answers = file.readlines()

    return render_template("results.html", answers=answers)


if __name__ == "__main__":
    app.run(debug=True)