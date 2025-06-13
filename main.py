from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

#df = pd.read_csv("")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt") # zfill(6)
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)