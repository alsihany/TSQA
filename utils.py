import json
import pandas as pd
from fuzzywuzzy import fuzz

def process_question(question):
    with open("laws_database.json", encoding="utf-8") as f:
        data = json.load(f)

    النتائج = []
    for item in data:
        درجة_التشابه = fuzz.partial_ratio(question, item["النص"])
        if درجة_التشابه >= 70:  # يمكنك تعديل الرقم حسب درجة الحساسية
            النتائج.append(f"📘 {item['النظام']} - {item['رقم']}:\n{item['النص']}")

    if not النتائج:
        return {"answer": "لم يتم العثور على نتائج لهذا السؤال."}

    summary = "🧾 هذه المعلومات حسب الأنظمة السعودية حتى تاريخ 2025:\n\n"
    return {"answer": summary + "\n\n".join(النتائج)}
