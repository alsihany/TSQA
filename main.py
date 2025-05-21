from flask import Flask, request, jsonify, render_template
from utils import process_question
import urllib.parse

app = Flask(__name__, template_folder='.')

@app.route("/ask")
def ask():
    question = request.args.get("q", "")
    if not question:
        return jsonify({"error": "يرجى إدخال سؤال في الرابط مثل /ask?q=سؤالك"})
    result = process_question(question)
    return jsonify(result)

@app.route("/share")
def share():
    text = request.args.get("text", "")
    return render_template("share.html", text=text)

@app.route("/")
def home():
    return "<h3>✅ TSQA Bot يعمل! استخدم /ask?q=سؤالك</h3>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
