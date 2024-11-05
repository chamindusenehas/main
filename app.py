from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb+srv://chamindusenehas:Chamee.19721@techverse.msx3fg5.mongodb.net/?retryWrites=true&w=majority&appName=techverse')
db = client["quiz"]
scores_collection = db["students"]

@app.route("/scores", methods=["GET"])
def get_scores():
    scores = []
    for entry in scores_collection.find():
        scores.append({"name": entry["school"], "score": entry["quiz-score"]})
    return jsonify(scores)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
