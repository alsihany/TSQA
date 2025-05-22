from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# تحميل قاعدة المعرفة
with open("knowledge_base.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# البحث عن إجابة
def find_answer(query):
    for item in knowledge:
        if item["question"] in query:
            return item["answer"]
    return "لم يتم العثور على نتائج لهذا السؤال"

@app.route("/ask")
def ask():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"error": "يرجى إدخال سؤال"}), 400
    answer = find_answer(q)
    return jsonify({"question": q, "answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)