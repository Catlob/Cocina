import time
import random
import webbrowser
from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("test.html")


@app.route("/result", methods=["POST"])
def result():
    links = []
    rate = [i/10 for i in range(10)]
    output = request.form.to_dict()
    text = output["search"]
    query = "Recetas " + str(text)
    time.sleep(10)
    for j in search(query, tld='com', lang='es', num=100, stop=100):
        time.sleep(random.choice(rate))
        print(query)
        print(j)
        links.append(j)
    print(links)

    return render_template("test.html", link=random.choice(links), linv=random.choice(links),
                           lin=random.choice(links),
                           linr=random.choice(links), lon=random.choice(links), text=text)


@app.route("/buyPage", methods=["POST"])
def buyPage():

    return render_template("buy_pag.html")


@app.route("/buyingResult", methods=["POST"])
def buyingResult():
    rate = [i/10 for i in range(10)]
    output = request.form.to_dict()
    text = output["buy"]
    query = "Corneshop comprar " + str(text)
    for j in search(query, tld='com', lang='es', num=1):
        print(j)
        time.sleep(random.choice(rate))
    webbrowser.open_new_tab(j)

    return render_template("buy_pag.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
