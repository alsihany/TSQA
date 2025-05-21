import json
import pandas as pd

def process_question(question):
    with open("laws_database.json", encoding="utf-8") as f:
        data = json.load(f)

    matches = []
    for item in data:
        if question in item["النص"]:
            matches.append(f"📘 {item['النظام']} - {item['رقم']}:\n{item['النص']}")

    if not matches:
        return {"answer": "لم يتم العثور على نتائج لهذا السؤال."}

    summary = "🧾 هذه المعلومات حسب الأنظمة السعودية حتى تاريخ 2025:\n\n"
    return {"answer": summary + "\n\n".join(matches)}