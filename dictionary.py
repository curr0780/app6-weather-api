from flask import Flask, render_template
import pandas as pd

df = pd.read_csv("dictionary.csv")
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_dict.html")

@app.route("/api/v1/<word>")
def api(word):
    word_def = df.loc[df['word'] == word]['definition'].iloc[0]
    return {"definition": word_def,
            "word": word,
            }


# if __name__ == "__main__":
app.run(debug=True, port=5001)