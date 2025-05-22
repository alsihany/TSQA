import json
import pandas as pd
import difflib

def process_question(question):
    with open("laws_database.json", encoding="utf-8") as f:
        data = json.load(f)

    النصوص = [item["النص"] for item in data]
    matches = difflib.get_close_matches(question, النصوص, n=3, cutoff=0.3)

    النتائج = []
    for item in data:
        if item["النص"] in matches:
            النتائج.append(f"📘 {item['النظام']} - {item['رقم']}:\n{item['النص']}")

    if not النتائج:
        return {"answer": "لم يتم العثور على نتائج لهذا السؤال."}

    summary = "🧾 هذه المعلومات حسب الأنظمة السعودية حتى تاريخ 2025:\n\n"
    return {"answer": summary + "\n\n".join(النتائج)}
