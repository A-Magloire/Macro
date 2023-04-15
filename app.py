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
        Inflation_Rate = request.form["Inflation_Rate"]
        GDP_Growth = request.form["GDP_Growth"]
        Unemployment_Rate = request.form["Unemployment_Rate"]
        Stock_Market_Growth = request.form["Stock_Market_Growth"]
        Public_Debt = request.form["Public_Debt"]

        # Generate SWOT analysis using OPENAI's chat completions API
        prompt = f"In 200 words, interpret the state of the economy and provide the best industry and company recommendations for investment given the following economic data: Interest rate: {Interest_Rate}, Inflation rate: {Inflation_Rate}, GDP growth: {GDP_Growth}, Unemployment rate: {Unemployment_Rate}, Annual Stock Market Growth: {Stock_Market_Growth}, Public Debt: {Public_Debt}. "
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=250,
            n=1,
            temperature=0.8,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# Overnight Interest Rate = 4.5%
# Inflation Rate = 5.9% 
# GDP Growth = 1.1% YoY
# Unemployment Rate = 5%
# Stock Market Growth = -0.21% YoY
# Public Debt = 58.2% of GDP

# def generate_prompt(animal):
#     return """Provide a SWOT analysis for the following company, complete with statistics.
# Company: {}"""