import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # get company name from the front end
        Interest_Rate = request.form["Interest_Rate"]

        # Generate SWOT analysis using OPENAI's chat completions API
        prompt = f"In 50 words or less, interpret the state of the economy given the following economic data: Interest rate: {Interest_Rate}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Provide a SWOT analysis for the following company, complete with statistics.
# Company: {}"""